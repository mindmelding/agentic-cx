"""Tests for scripts/cx. Run: python3 scripts/test_cx.py"""

import importlib.machinery
import importlib.util
import datetime
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
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



EXAMPLE_SPEC = cx.ROOT / "templates" / "spec" / "answer_behavior_question.yaml"


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


class SpecParse(unittest.TestCase):
    def test_fallback_reads_the_example_like_pyyaml(self):
        text = EXAMPLE_SPEC.read_text()
        with mock.patch.dict(sys.modules, {"yaml": None}):
            fallback = cx.parse_spec_yaml(text)
        self.assertEqual(fallback["class"], "answer_behavior_question")
        self.assertEqual(fallback["default_rung"], 3)
        self.assertEqual(len(fallback["never"]), 2)
        try:
            import yaml
        except ModuleNotFoundError:
            return
        self.assertEqual(fallback, yaml.safe_load(text))

    def test_fallback_refuses_what_it_cannot_read(self):
        with mock.patch.dict(sys.modules, {"yaml": None}):
            with self.assertRaises(cx.CxError):
                cx.parse_spec_yaml("fires_when: >\n  folded text\n")
            with self.assertRaises(cx.CxError):
                cx.parse_spec_yaml("nested:\n  key: value\n")

    def test_dispositions_take_the_triage_words(self):
        body = "Fix\n\ndoc: a_b = no-page\n- doc: `c_d`: promise-line\ndoc: e = Guide\n"
        self.assertEqual(cx.parse_dispositions(body), {"a_b": "spec-only", "c_d": "page", "e": "guide"})


class SpecSources(unittest.TestCase):
    def test_file_directory_and_glob(self):
        self.assertTrue(cx.source_matches("src/a.ts", "src/a.ts"))
        self.assertTrue(cx.source_matches("./src/a.ts", "src/a.ts"))
        self.assertTrue(cx.source_matches("src/analytics", "src/analytics/x/y.ts"))
        self.assertTrue(cx.source_matches("src/analytics/", "src/analytics/y.ts"))
        self.assertFalse(cx.source_matches("src/analytics", "src/analytics-old/y.ts"))
        self.assertTrue(cx.source_matches("src/**/*.ts", "src/a/b/c.ts"))
        self.assertTrue(cx.source_matches("src/**/*.ts", "src/c.ts"))
        self.assertFalse(cx.source_matches("src/**/*.ts", "lib/c.ts"))
        self.assertTrue(cx.source_matches(".github/workflows/ci.yml", ".github/workflows/ci.yml"))


class SpecLint(unittest.TestCase):
    def spec(self, **changes):
        data = cx.parse_spec_yaml(EXAMPLE_SPEC.read_text())
        data.update(changes)
        return cx.Spec("specs/x.yaml", data)

    def errors(self, *specs, repo=None):
        return [m for level, m in cx.lint_specs(list(specs), repo or Path("."), check_sources=repo is not None) if level == "error"]

    def test_the_example_is_clean(self):
        self.assertEqual(cx.lint_specs([self.spec()], Path("."), check_sources=False), [])

    def test_missing_field(self):
        data = cx.parse_spec_yaml(EXAMPLE_SPEC.read_text())
        del data["never"]
        self.assertTrue(any("`never`" in e for e in self.errors(cx.Spec("s.yaml", data))))

    def test_irreversible_never_silent(self):
        self.assertTrue(any("irreversible" in e for e in self.errors(self.spec(reversible="no. Sent mail stays sent"))))
        self.assertTrue(any("irreversible" in e for e in self.errors(self.spec(reversible=False))))

    def test_rung_range_and_duplicates(self):
        self.assertTrue(self.errors(self.spec(default_rung=5)))
        self.assertTrue(any("also defined" in e for e in self.errors(self.spec(), self.spec())))

    def test_missing_source_and_template_placeholders(self):
        repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, repo)
        self.assertTrue(any("does not exist" in e for e in self.errors(self.spec(), repo=repo)))
        template = cx.parse_spec_yaml(cx.SPEC_TEMPLATE.format(name="x"))
        self.assertTrue(any("placeholders" in e for e in self.errors(cx.Spec("t.yaml", template))))


class SpecCheck(unittest.TestCase):
    """A product repo with the example spec, and a branch that changes it."""

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo)
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.email", "t@example.com")
        git(self.repo, "config", "user.name", "t")
        (self.repo / "src" / "analytics").mkdir(parents=True)
        for name in ("answer.ts", "what-changed.ts"):
            (self.repo / "src" / "analytics" / name).write_text("x\n")
        (self.repo / "README.md").write_text("x\n")
        (self.repo / "specs").mkdir()
        shutil.copy(EXAMPLE_SPEC, self.repo / "specs")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-qm", "base")
        git(self.repo, "checkout", "-qb", "change")

    def commit(self, path, text):
        (self.repo / path).write_text(text)
        git(self.repo, "commit", "-qam", "change")

    def check(self, body="", require_all=False):
        specs = cx.load_specs(self.repo / "specs", self.repo)
        touched = cx.affected(specs, cx.changed_paths(self.repo, "main"), self.repo, "main", self.repo / "specs")
        decided = cx.parse_dispositions(body)
        for t in touched:
            t.disposition = decided.get(t.spec.name, "")
        return touched, cx.gate(touched, require_all)

    def move_never(self):
        path = self.repo / "specs" / "answer_behavior_question.yaml"
        self.commit("specs/answer_behavior_question.yaml", path.read_text().replace("never:\n", "never:\n  - export raw events\n"))

    def test_untouched_change_names_nothing(self):
        self.commit("README.md", "y\n")
        self.assertEqual(self.check(), ([], {}))

    def test_source_change_is_unverified_not_blocking(self):
        self.commit("src/analytics/what-changed.ts", "y\n")
        touched, blocking = self.check()
        self.assertEqual([t.spec.name for t in touched], ["answer_behavior_question"])
        self.assertEqual(touched[0].paths, ["src/analytics/what-changed.ts"])
        self.assertFalse(touched[0].never_changed)
        self.assertEqual(blocking, {})
        self.assertTrue(self.check(require_all=True)[1])

    def test_moved_never_waits_for_a_person(self):
        self.move_never()
        touched, blocking = self.check()
        self.assertTrue(touched[0].never_changed)
        self.assertIn(touched[0], blocking)

    def test_moved_never_is_not_cleared_by_no_page(self):
        self.move_never()
        self.assertTrue(self.check("doc: answer_behavior_question = no-page")[1])
        self.assertEqual(self.check("doc: answer_behavior_question = update")[1], {})

    def test_unknown_disposition_blocks(self):
        self.commit("src/analytics/answer.ts", "y\n")
        self.assertTrue(self.check("doc: answer_behavior_question = later")[1])

    def test_a_new_spec_is_new(self):
        shutil.copy(EXAMPLE_SPEC, self.repo / "specs" / "second.yaml")
        path = self.repo / "specs" / "second.yaml"
        path.write_text(path.read_text().replace("class: answer_behavior_question", "class: warn_activation_drop"))
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-qm", "new")
        touched, blocking = self.check()
        new = [t for t in touched if t.spec.name == "warn_activation_drop"][0]
        self.assertTrue(new.new)
        self.assertIn(new, blocking)

    def test_a_deleted_spec_waits_for_a_person(self):
        git(self.repo, "rm", "-q", "specs/answer_behavior_question.yaml")
        git(self.repo, "commit", "-qm", "drop")
        touched, blocking = self.check()
        self.assertEqual([(t.spec.name, t.removed) for t in touched], [("answer_behavior_question", True)])
        self.assertIn(touched[0], blocking)
        self.assertEqual(self.check("doc: answer_behavior_question = remove")[1], {})

    def test_cli_exit_codes_and_markdown(self):
        self.move_never()
        out = io.StringIO()
        with redirect_stdout(out):
            code = cx.main(["spec", "check", "--repo", str(self.repo), "--base", "main", "--format", "markdown"])
        self.assertEqual(code, 1)
        self.assertTrue(out.getvalue().startswith(cx.COMMENT_MARKER))
        self.assertIn("doc: answer_behavior_question = update", out.getvalue())
        body = self.repo / "body.md"
        body.write_text("doc: answer_behavior_question = update\n")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(cx.main(["spec", "check", "--repo", str(self.repo), "--base", "main", "--body-file", str(body)]), 0)

    def test_spec_new_never_overwrites(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(cx.main(["spec", "new", "--repo", str(self.repo), "warn_activation_drop"]), 0)
        with redirect_stderr(io.StringIO()):
            self.assertEqual(cx.main(["spec", "new", "--repo", str(self.repo), "warn_activation_drop"]), 2)
            self.assertEqual(cx.main(["spec", "new", "--repo", str(self.repo), "Bad-Name"]), 2)



STATE = cx.ROOT / "templates" / "house" / "state"


class StateTemplates(unittest.TestCase):
    def test_stack_template_has_every_capability_in_tools(self):
        data, problems = cx.load_stack(STATE / "stack.md")
        self.assertEqual([p for p in problems if "ledger_level" not in p[2] and "updated" not in p[2]], [])
        have = {(r["section"], r["capability"]) for r in data["capabilities"]}
        want = {(s, c) for s, names in cx.capabilities().items() for c in names}
        self.assertEqual(have, want)
        self.assertEqual(len(want), 24)

    def test_queue_templates_read_clean(self):
        self.assertEqual(cx.load_voice(STATE / "voice-queue.md")[1], [])
        self.assertEqual(cx.load_inbox(STATE / "context-inbox.md")[1], [])

    def test_init_copies_the_queue_templates(self):
        house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, house)
        cx.init_house(house)
        self.assertEqual((house / "voice-queue.md").read_text(), (STATE / "voice-queue.md").read_text())


class StateParse(unittest.TestCase):
    def setUp(self):
        self.house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.house)
        cx.init_house(self.house)

    def write(self, name, text, append=True):
        path = self.house / name
        path.write_text((path.read_text() if append and path.exists() else "") + text)
        return path

    def test_queue_rows_escapes_and_bad_rows(self):
        path = self.write("voice-queue.md",
                          "| CSV import fails | \"spins\" | Acme | Split it | 3 | t-412 | pass | open |\n"
                          "| Retries \\| dupes | \"twice\" | Beta | Dedupe | 1 | t-88 | hold | held: second report |\n"
                          "| Short | row |\n"
                          "| Bad | q | a | r | many | e | maybe | done |\n")
        data, problems = cx.load_voice(path)
        self.assertEqual([r["Flaw"] for r in data["items"]], ["CSV import fails", "Retries | dupes", "Bad"])
        messages = " ".join(m for _, _, m in problems)
        for expected in ("2 cells", "Count is a whole number", "State is open", "Proposal is pass or hold"):
            self.assertIn(expected, messages)

    def test_cursor_must_be_never_or_a_time(self):
        path = self.house / "voice-queue.md"
        path.write_text(path.read_text().replace("cursor: never", "cursor: yesterday"))
        self.assertTrue(any("cursor" in m for _, _, m in cx.load_voice(path)[1]))
        path.write_text(path.read_text().replace("cursor: yesterday", "cursor: 2026-10-08T08:45:00-07:00"))
        self.assertEqual(cx.load_voice(path)[1], [])

    def test_stack_lines(self):
        text = (STATE / "stack.md").read_text().replace("updated: YYYY-MM-DD", "updated: 2026-10-01")
        text = text.replace("- Memory store: absent, not yet assessed", "- Memory store: found, Postgres memories")
        text = text.replace("- Renderer: absent, not yet assessed", "- Renderer: maybe Mintlify")
        text += "- Gong: call summaries\n"
        data, problems = cx.load_stack(self.write("stack.md", text, append=False))
        memory = [r for r in data["capabilities"] if r["capability"] == "Memory store"][0]
        self.assertEqual((memory["status"], memory["where"]), ("found", "Postgres memories"))
        self.assertEqual(data["inward"], [{"tool": "Gong", "does": "call summaries"}])
        self.assertEqual(data["ledger_level"], 0)
        self.assertTrue(any("`Renderer` needs found" in m for _, _, m in problems))
        self.assertTrue(any("no line for Documentation: Renderer" in m for _, _, m in problems))

    def test_status_board(self):
        self.write("voice-queue.md", "| CSV | q | Acme | r | 2 | e | pass | open |\n| W | q | B | r | 1 | e | hold | passed: https://x/1 |\n")
        self.write("context-inbox.md", "| 2026-10-07 | Acme | Fiscal year starts in February | sam | call |\n")
        self.write("local/learnings/days/2026-10-07.md", "# 2026-10-07\n\n## Landed\n## Still open\n- CSV row\n- a spec\n")
        self.write("local/runs/2026-10-07-close.md", "note\n<!-- exit 1 -->\n")
        status, problems = cx.house_status(self.house)
        self.assertEqual(problems, [])
        board = dict(cx.status_lines(status, problems, today=THURSDAY))
        self.assertIn("1 waiting on pass or hold", board["Voice"])
        self.assertIn("1 passed", board["Voice"])
        self.assertIn("1 fact(s)", board["Context"])
        self.assertEqual(board["Day note"], "2026-10-07, 2 still open")
        self.assertEqual(board["Runs"], "close 2026-10-07 (exit 1)")
        self.assertIn("not run", board["Setup"])

    def test_doctor_names_unreadable_lines(self):
        shutil.copy(cx.ROOT / ".gitignore", self.house / ".gitignore")
        subprocess.run(["git", "init", "-q", str(self.house)], check=True)
        self.write("voice-queue.md", "| Short | row |\n")
        warnings = [m for level, m in cx.doctor(self.house) if level == "warn"]
        self.assertTrue(any(m.startswith("voice-queue.md:") and "cells" in m for m in warnings))



class House(unittest.TestCase):
    def test_defaults_to_the_repo(self):
        with mock.patch.dict(cx.os.environ, {"CX_HOUSE": ""}):
            self.assertEqual(cx.house_dir(), cx.ROOT)

    def test_cx_house_moves_it(self):
        house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, house)
        with mock.patch.dict(cx.os.environ, {"CX_HOUSE": str(house)}):
            self.assertEqual(cx.house_dir(), house.resolve())

    def test_a_house_outside_git_passes_doctor(self):
        house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, house)
        cx.init_house(house)
        results = cx.doctor(house)
        self.assertNotIn("fail", {level for level, _ in results})
        self.assertTrue(any("outside any git repository" in m for _, m in results))

    def test_run_points_at_the_kit_and_works_in_the_house(self):
        command, *_ = cx.run_plan(MODELS, consent(), "open", "claude", kit=Path("/kit"), house=Path("/house"), today=THURSDAY)
        prompt = command[command.index("-p") + 1]
        self.assertIn("Run /kit/skills/open/SKILL.md", prompt)
        self.assertEqual(command.count("--add-dir"), 2)


def rpc(server, method, params=None, mid=1):
    message = {"jsonrpc": "2.0", "id": mid, "method": method}
    if params is not None:
        message["params"] = params
    return server.handle(message)


def tool(server, name, **arguments):
    result = rpc(server, "tools/call", {"name": name, "arguments": arguments})["result"]
    return result["content"][0]["text"], result["isError"]


class Mcp(unittest.TestCase):
    def setUp(self):
        self.house = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.house)
        cx.init_house(self.house)
        self.server = cx.McpServer(house=self.house)

    def test_initialize_echoes_the_version_and_names_the_rules(self):
        result = rpc(self.server, "initialize", {"protocolVersion": "2025-03-26"})["result"]
        self.assertEqual(result["protocolVersion"], "2025-03-26")
        self.assertEqual(set(result["capabilities"]), {"resources", "prompts", "tools"})
        self.assertIn("Customer data never enters git", result["instructions"])

    def test_notifications_get_no_reply(self):
        self.assertIsNone(self.server.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}))

    def test_unknown_method(self):
        self.assertEqual(rpc(self.server, "sampling/createMessage")["error"]["code"], -32601)

    def test_resources_are_the_manual_and_never_private_files(self):
        uris = [r["uri"] for r in rpc(self.server, "resources/list")["result"]["resources"]]
        self.assertIn("cx://manual/skills/open/SKILL.md", uris)
        self.assertIn("cx://manual/templates/house/state/stack.md", uris)
        for private in ("stack.md", "voice-queue.md", "context-inbox.md"):
            self.assertNotIn("cx://manual/" + private, uris)
        self.assertFalse(any(u.startswith("cx://manual/local/") or "/.git" in u for u in uris))
        text = rpc(self.server, "resources/read", {"uri": "cx://manual/routines.md"})["result"]["contents"][0]["text"]
        self.assertTrue(text.startswith("# Routines"))

    def test_links_resolve_from_the_file_they_are_in(self):
        text, error = tool(self.server, "manual_read", path="../../routines.md", **{"from": "skills/open/SKILL.md"})
        self.assertFalse(error)
        self.assertIn("# Routines", text)
        text, error = tool(self.server, "manual_read", path="floor/moments/first-reply")
        self.assertFalse(error)

    def test_nothing_outside_the_manual(self):
        for path in ("../../../etc/passwd", "stack.md", "local/consent.toml", ".git/config", "/etc/passwd"):
            _, error = tool(self.server, "manual_read", path=path)
            self.assertTrue(error, path)

    def test_prompts_are_the_skills(self):
        names = [p["name"] for p in rpc(self.server, "prompts/list")["result"]["prompts"]]
        self.assertEqual(names, list(cx.SKILL_FILES))
        text = rpc(self.server, "prompts/get", {"name": "open"})["result"]["messages"][0]["content"]["text"]
        self.assertIn("# Open", text)
        self.assertIn(str(self.house), text)
        self.assertNotIn("name: cx-open", text)
        self.assertEqual(rpc(self.server, "prompts/get", {"name": "nope"})["error"]["code"], -32602)

    def test_lexicon_and_search(self):
        text, _ = tool(self.server, "lexicon_check", text="Great question! We leverage it.")
        self.assertTrue(text.startswith("FAIL"))
        text, _ = tool(self.server, "lexicon_check", text="Fixed on our side. The import runs again.")
        self.assertEqual(text, "PASS")
        text, _ = tool(self.server, "manual_search", query="context floor", limit=3)
        self.assertEqual(len(text.splitlines()), 4)

    def test_status_and_doctor_read_the_house(self):
        text, error = tool(self.server, "cx_status")
        self.assertFalse(error)
        self.assertIn(f"House: {self.house}", text)
        text, _ = tool(self.server, "cx_doctor")
        self.assertIn("Initialized", text)

    def test_a_broken_lexicon_is_an_error_not_an_exit(self):
        with mock.patch.object(cx, "load_lexicon", side_effect=SystemExit("cx: lexicon is missing blocks")):
            reply = rpc(self.server, "tools/call", {"name": "lexicon_check", "arguments": {"text": "x"}})
        self.assertEqual(reply["error"]["code"], -32603)

    def test_serve_over_stdio(self):
        lines = [json.dumps({"jsonrpc": "2.0", "id": 1, "method": "ping"}), "not json",
                 json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"})]
        out = io.StringIO()
        self.server.serve(io.StringIO("\n".join(lines) + "\n"), out)
        replies = [json.loads(l) for l in out.getvalue().splitlines()]
        self.assertEqual(replies[0], {"jsonrpc": "2.0", "id": 1, "result": {}})
        self.assertEqual(replies[1]["error"]["code"], -32700)
        self.assertEqual(len(replies), 2)


class McpConfig(unittest.TestCase):
    def test_each_host_gets_a_working_snippet(self):
        house = Path("/srv/acme-cx")
        for host in cx.MCP_HOSTS:
            text = cx.mcp_config(host, house)
            self.assertIn("mcp", text)
            self.assertIn("/srv/acme-cx", text)
            body = "\n".join(l for l in text.splitlines() if not l.startswith(("//", "# ")))
            if host == "claude":
                self.assertTrue(text.startswith("claude mcp add agentic-cx --scope user -e CX_HOUSE=/srv/acme-cx -- "))
            elif host == "codex":
                self.assertEqual(cx.tomllib.loads(body)["mcp_servers"]["agentic-cx"]["env"]["CX_HOUSE"], "/srv/acme-cx")
            else:
                data = json.loads(body)
                server = (data.get("servers") or data["mcpServers"])["agentic-cx"]
                self.assertEqual(server["args"][-2:], ["mcp", "serve"])

    def test_without_a_house_there_is_no_env(self):
        self.assertNotIn("CX_HOUSE", cx.mcp_config("json"))


if __name__ == "__main__":
    unittest.main()
