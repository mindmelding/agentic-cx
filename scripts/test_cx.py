"""Tests for scripts/cx. Run: python3 scripts/test_cx.py"""

import importlib.machinery
import importlib.util
import datetime
import io
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
loader = importlib.machinery.SourceFileLoader("cx", str(HERE / "cx"))
spec = importlib.util.spec_from_loader("cx", loader)
cx = importlib.util.module_from_spec(spec)
loader.exec_module(cx)

LEX = cx.load_lexicon()


def kinds(text, errors_only=True):
    return [f.kind for f in cx.check_text(text, LEX, "t") if not (errors_only and f.warning)]


class LexiconLoads(unittest.TestCase):
    def test_every_block_is_populated(self):
        self.assertIn("great question", LEX.phrases)
        self.assertIn("leverage", LEX.words)
        self.assertIn("Unfortunately", LEX.openers)
        self.assertTrue(any(src == " — " for src, _ in LEX.patterns), "spaced em dash keeps its spaces")


class Catches(unittest.TestCase):
    def test_phrase_ignores_case_and_curly_quotes(self):
        self.assertIn("banned phrase", kinds("Please don’t HESITATE to reach out."))

    def test_word_needs_whole_word(self):
        self.assertIn("banned word", kinds("We leverage the data."))
        self.assertEqual(kinds("Every delivery was verified."), [])

    def test_opener_skips_subject_and_greeting(self):
        text = "Subject: Your invoice\n\nHi Dana,\n\nUnfortunately the credit failed."
        self.assertIn("banned opener", kinds(text))

    def test_opener_only_at_the_start(self):
        self.assertNotIn("banned opener", kinds("Fixed. Certainly a strange one."))

    def test_structural_tells(self):
        self.assertIn("structural tell", kinds("It's not a bug, it's a feature."))
        self.assertIn("structural tell", kinds("Done — all of it."))
        self.assertIn("structural tell", kinds("Wait..."))

    def test_unspaced_em_dash_is_allowed(self):
        self.assertEqual(kinds("Done—all of it."), [])

    def test_code_is_ignored(self):
        self.assertEqual(kinds("Run this:\n\n```\nleverage --robust\n```\n\nThen `utilize` it."), [])

    def test_blockquote_markers_are_ignored(self):
        self.assertIn("banned opener", kinds("> Hi Dana,\n>\n> Unfortunately it failed."))

    def test_line_numbers_are_offset(self):
        [f] = [f for f in cx.check_text("ok\nwe leverage it", LEX, "t", first_line=10) if not f.warning]
        self.assertEqual((f.line, f.col), (11, 4))

    def test_substitute_hint(self):
        [f] = cx.check_text("We utilize it.", LEX, "t")
        self.assertEqual(f.hint, "use")


class Warnings(unittest.TestCase):
    def test_two_exclamations_warn(self):
        found = cx.check_text("Done! Shipped!", LEX, "t")
        self.assertEqual([f.kind for f in found if f.warning], ["more than one exclamation point"])

    def test_two_apologies_warn(self):
        found = cx.check_text("Sorry about Tuesday. We apologize again.", LEX, "t")
        self.assertTrue(any(f.warning and "apologized" in f.kind for f in found))


class Clean(unittest.TestCase):
    def test_a_good_reply_passes(self):
        text = (
            "Subject: Your August invoice, corrected\n\nHi Dana,\n\n"
            "The 12-seat line was two prorated adds on the 3rd. Net $18, which I've credited (ref 4471).\n\n"
            "Want me to remove the two?\n\nSam"
        )
        self.assertEqual(cx.check_text(text, LEX, "t"), [])

    def test_repo_corpus_is_clean(self):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cx.main(["check", "--gold", "--templates", "--quiet"])
        self.assertEqual(code, 0, out.getvalue())


class Cli(unittest.TestCase):
    def test_no_target_is_a_usage_error(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(cx.main(["check"]), 2)



class Init(unittest.TestCase):
    def setUp(self):
        self.house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.house)

    def test_creates_the_private_files(self):
        created, kept = cx.init_house(self.house)
        for rel in ("local/consent.toml", "voice-queue.md", "context-inbox.md", "local/overlay/authority.md", "local/learnings/index.md"):
            self.assertIn(rel, created)
        self.assertTrue((self.house / "local" / "learnings" / "days").is_dir())
        self.assertEqual(kept, [])

    def test_never_overwrites(self):
        cx.init_house(self.house)
        queue = self.house / "voice-queue.md"
        queue.write_text("mine", encoding="utf-8")
        created, kept = cx.init_house(self.house)
        self.assertEqual(created, [])
        self.assertIn("voice-queue.md", kept)
        self.assertEqual(queue.read_text(encoding="utf-8"), "mine")

    def test_default_consent_allows_nothing(self):
        cx.init_house(self.house)
        consent = cx.load_consent(self.house)
        self.assertFalse(any(consent["read"].values()))
        self.assertEqual(cx.allowed_connectors(consent), [])
        self.assertEqual(consent["unattended"]["skills"], list(cx.UNATTENDED))


class Doctor(unittest.TestCase):
    def setUp(self):
        self.house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.house)
        shutil.copy(cx.ROOT / ".gitignore", self.house / ".gitignore")
        subprocess.run(["git", "init", "-q", str(self.house)], check=True)

    def levels(self):
        return {level for level, _ in cx.doctor(self.house)}

    def test_fails_before_init(self):
        self.assertIn("fail", self.levels())

    def test_passes_after_init(self):
        cx.init_house(self.house)
        self.assertNotIn("fail", self.levels())

    def test_fails_when_private_files_are_tracked(self):
        (self.house / ".gitignore").write_text("", encoding="utf-8")
        cx.init_house(self.house)
        self.assertTrue(any(level == "fail" and "gitignored" in m for level, m in cx.doctor(self.house)))

    def test_fails_on_a_skill_that_cannot_run_unattended(self):
        cx.init_house(self.house)
        path = self.house / "local" / "consent.toml"
        path.write_text(path.read_text().replace('skills = ["open", "close"]', 'skills = ["open", "triage"]'))
        self.assertIn("fail", self.levels())


MODELS = cx.load_models()
THURSDAY, FRIDAY = datetime.date(2026, 10, 8), datetime.date(2026, 10, 9)


def consent(connectors=(), skills=cx.UNATTENDED):
    return {"read": {}, "connectors": {"allowed": list(connectors)}, "unattended": {"skills": list(skills)}}


class Run(unittest.TestCase):
    def plan(self, skill="open", harness="claude", c=None, today=THURSDAY):
        return cx.run_plan(MODELS, consent() if c is None else c, skill, harness, kit=Path("/kit"), house=Path("/kit"), today=today)

    def test_claude_is_scoped_to_the_private_files(self):
        command, tier, model, scoped = self.plan()
        self.assertTrue(scoped)
        self.assertEqual((tier, model), ("fast", "haiku"))
        allow = command[command.index("--allowedTools") + 1:]
        self.assertIn("Edit(local/**)", allow)
        self.assertNotIn("Read", allow)
        self.assertNotIn("--permission-mode", command)

    def test_one_add_dir_when_kit_and_house_match(self):
        command, *_ = self.plan()
        self.assertEqual(command.count("--add-dir"), 1)

    def test_consented_connectors_join_the_allow_list(self):
        command, *_ = self.plan(c=consent(["moonbase", "bad name"]))
        self.assertIn("mcp__moonbase", command)
        self.assertFalse(any("bad" in t for t in command))

    def test_empty_model_drops_the_flag(self):
        command, _, model, scoped = self.plan(harness="codex")
        self.assertEqual(model, "")
        self.assertNotIn("-m", command)
        self.assertFalse(scoped)

    def test_friday_close_takes_the_friday_tier(self):
        self.assertEqual(self.plan("close", today=THURSDAY)[1], "standard")
        self.assertEqual(self.plan("close", today=FRIDAY)[1], "frontier")

    def test_prompt_carries_the_date_and_the_rules(self):
        command, *_ = self.plan()
        prompt = command[command.index("-p") + 1]
        self.assertIn("Thursday 2026-10-08", prompt)
        self.assertIn("skills/open/SKILL.md", prompt)
        self.assertIn("local/consent.toml", prompt)

    def test_refuses_skills_that_wait_on_a_person(self):
        for skill in ("setup", "floor", "triage", "refresh"):
            with self.assertRaises(cx.CxError):
                self.plan(skill)

    def test_refuses_what_consent_leaves_out(self):
        with self.assertRaises(cx.CxError):
            self.plan("close", c=consent(skills=["open"]))

    def test_refuses_before_init(self):
        with self.assertRaises(cx.CxError):
            cx.run_plan(MODELS, None, "open", "claude")

    def test_refusal_exits_2(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(cx.main(["run", "triage", "--harness", "claude", "--dry-run"]), 2)


if __name__ == "__main__":
    unittest.main()
