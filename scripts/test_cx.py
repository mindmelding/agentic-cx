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


if __name__ == "__main__":
    unittest.main()
