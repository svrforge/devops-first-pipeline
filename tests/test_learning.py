import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import learn
from scripts.validate_course import validate


class LearningTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'progress.json'
        self.patch = patch.dict(os.environ, {'DEVOPS_PROGRESS_FILE': str(self.path)})
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def run_cli(self, args):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = learn.main(args)
        return code, output.getvalue()

    def test_default_is_english_and_does_not_write(self):
        code, output = self.run_cli([])
        self.assertEqual(code, 0)
        self.assertIn('What is DevOps?', output)
        self.assertFalse(self.path.exists())

    def test_english_day_lesson(self):
        code, output = self.run_cli(['lesson', '01'])
        self.assertEqual(code, 0)
        self.assertIn('Day 1', output)

    def test_quiz_rejects_wrong_and_accepts_right(self):
        self.assertEqual(self.run_cli(['quiz', '01', '--answer', '1'])[0], 1)
        self.assertEqual(self.run_cli(['quiz', '01', '--answer', '2'])[0], 0)
        self.assertFalse(self.path.exists())

    def test_completion_deduplicates_and_next_moves_on(self):
        self.run_cli(['complete', '01'])
        self.run_cli(['complete', '01'])
        self.assertEqual(json.loads(self.path.read_text()), ['01'])
        self.assertIn('lesson 02', self.run_cli(['next'])[1])

    def test_invalid_progress_is_not_overwritten(self):
        self.path.write_text('{broken')
        with self.assertRaises(SystemExit) as caught:
            self.run_cli(['complete', '01'])
        self.assertEqual(caught.exception.code, 2)
        self.assertEqual(self.path.read_text(), '{broken')

    def test_invalid_id_has_nonzero_exit(self):
        result = subprocess.run([sys.executable, 'learn.py', 'lesson', '99'], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)

    def test_course_and_links(self):
        validate()
