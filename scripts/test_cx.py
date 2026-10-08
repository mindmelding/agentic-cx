"""Tests for scripts/cx. Run: python3 scripts/test_cx.py"""

import importlib.machinery
import importlib.util
import io
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


import datetime
import tempfile
import textwrap

TODAY = datetime.date(2026, 10, 30)


def item(n, kind, rung="draft", status="open", opened="2026-10-29", extra=""):
    return textwrap.dedent(f"""
    ### Q-{n:04d} · {kind} · Acme
    - why: test
    - source: inbox
    - handler: test
    - rung: {rung}
    - sensitive: no
    - opened: {opened}
    - status: {status}
    """) + extra


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        with redirect_stdout(io.StringIO()):
            cx.main(["init", "--dir", self.tmp.name, "--today", "2026-10-01"])

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text, append=True):
        with open(self.dir / name, "a" if append else "w", encoding="utf-8") as f:
            f.write(text)

    def run_cx(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cx.main([*argv, "--dir", self.tmp.name, "--today", str(TODAY)])
        return code, out.getvalue(), err.getvalue()

    def test_init_writes_every_kind_at_its_start(self):
        kinds = cx.load_kinds()
        rungs = cx.parse_rungs((self.dir / "rungs.md").read_text())
        self.assertEqual(set(rungs), set(kinds))
        self.assertEqual(rungs["flaw-evidence"][0], "notice")
        self.assertEqual(rungs["incident"][0], "propose")

    def test_ceilings_are_read_from_the_manual(self):
        kinds = cx.load_kinds()
        self.assertEqual(kinds["reply-person"], ("draft", "draft"))
        self.assertEqual(kinds["fact"], ("draft", "silent"))
        self.assertEqual(kinds["doc-decision"], ("propose", "notice"))

    def test_order_is_band_then_due_then_age(self):
        self.write("queue.md", item(1, "setup", "propose", extra="- done when: x\n") + item(2, "fact") + item(3, "reply") + item(4, "incident", "propose"))
        code, out, _ = self.run_cx("queue")
        self.assertEqual(code, 0, out)
        self.assertEqual([l.split()[0] for l in out.splitlines()], ["Q-0003", "Q-0004", "Q-0001", "Q-0002"])

    def test_rung_above_ceiling_or_current_is_a_problem(self):
        self.write("queue.md", item(1, "reply-person", "notice") + item(2, "fact", "silent"))
        code, _, err = self.run_cx("queue")
        self.assertEqual(code, 1)
        self.assertIn("above the reply-person ceiling", err)
        self.assertIn("above the current fact rung", err)

    def test_sensitive_must_propose(self):
        self.write("queue.md", item(1, "reply").replace("sensitive: no", "sensitive: yes, a refund"))
        code, _, err = self.run_cx("queue")
        self.assertEqual(code, 1)
        self.assertIn("sensitive item must run at propose", err)

    def test_setup_needs_done_when(self):
        self.write("queue.md", item(1, "setup", "propose"))
        _, _, err = self.run_cx("queue")
        self.assertIn("without 'done when'", err)

    def test_expire_marks_and_logs_only_stale_open_items(self):
        self.write("queue.md", item(1, "fact", opened="2026-10-01") + item(2, "fact", status="blocked", opened="2026-10-01")
                   + item(3, "fact", opened="2026-10-01", extra="- touched: 2026-10-25\n"))
        self.run_cx("queue", "--expire", "--apply")
        q = (self.dir / "queue.md").read_text()
        self.assertIn("### Q-0001 · fact · Acme", q)
        self.assertEqual([i["fields"]["status"] for i in cx.parse_blocks(q, "Q")], ["expired", "blocked", "open"])
        self.assertIn("| Q-0001 | fact | draft |", (self.dir / "log.md").read_text())

    def log(self, start, kind, dispositions, rung="draft", day="2026-10-20", edit="", source=""):
        lines = [f"{day} | Q-{start + i:04d} | {kind} | {rung} | proposed | {d} | {edit} | {source}\n" for i, d in enumerate(dispositions)]
        self.write("log.md", "".join(lines))

    def test_promotion_needs_twenty_clean_at_the_rung(self):
        self.log(1, "fact", ["accepted"] * 19 + ["done"])
        report = self.run_cx("report")[1]
        self.assertIn("- fact: draft -> notice", report)

    def test_one_edit_in_the_run_blocks_promotion(self):
        self.log(1, "fact", ["accepted"] * 10 + ["edited"] + ["accepted"] * 9)
        self.assertNotIn("- fact: draft -> notice", self.run_cx("report")[1])

    def test_promotion_waits_two_weeks_at_the_rung(self):
        self.write("rungs.md", "| fact | draft | 2026-10-25 | demoted |\n")
        self.log(1, "fact", ["accepted"] * 20, day="2026-10-26")
        self.assertNotIn("- fact: draft -> notice", self.run_cx("report")[1])

    def test_no_promotion_past_the_ceiling(self):
        self.write("rungs.md", "| reply-person | draft | 2026-09-01 | start |\n")
        self.log(1, "reply-person", ["accepted"] * 25)
        self.assertNotIn("- reply-person:", self.run_cx("report")[1].split("### Rungs that should")[0].split("### Ready")[1])

    def test_rejection_flags_a_demotion(self):
        self.log(1, "reply", ["accepted"] * 5 + ["rejected"])
        report = self.run_cx("report")[1]
        self.assertIn("- reply: 1 rejected or reversed at draft", report)

    def test_three_edits_are_listed_for_a_rule(self):
        self.log(1, "reply", ["edited"] * 3, edit="cut the second paragraph")
        self.assertIn('Q-0001 "cut the second paragraph"', self.run_cx("report")[1])

    def test_five_drops_from_a_source_flag_the_producer(self):
        self.log(1, "check", ["dropped"] * 5, source="idle-facts")
        self.assertIn("- source idle-facts: last 5 dropped", self.run_cx("report")[1])

    def test_weekly_numbers(self):
        self.log(1, "fact", ["accepted", "accepted", "edited", "rejected"], day="2026-10-28")
        report = self.run_cx("report")[1]
        self.assertIn("| fact | draft | 4 | 2 | 1 | 1 |", report)
        self.assertIn("Closed without an operator edit: 50% of 4", report)

    def test_bridges_stuck_and_rising(self):
        self.write("bridges.md", textwrap.dedent("""
        ### B-001 · documentation · help center
        - baseline: 412 on 2026-09-01
        - now: 380
        - last moved: 2026-09-15

        ### B-002 · value · old scorecard
        - baseline: 3 reports on 2026-10-01
        - now: 4
        - last moved: 2026-10-20
        """))
        report = self.run_cx("report")[1]
        self.assertIn("B-001 help center: 412 -> 380 (-8%); last moved 2026-09-15 STUCK", report)
        self.assertIn("B-002 old scorecard: 3 -> 4 (33%); last moved 2026-10-20 ROSE", report)


if __name__ == "__main__":
    unittest.main()
