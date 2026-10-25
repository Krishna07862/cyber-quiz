
import os
import tempfile
import unittest
from unittest.mock import patch

import quiz


class TestCyberQuiz(unittest.TestCase):

    def test_has_30_questions(self):
        self.assertEqual(len(quiz.questions), 30)

    def test_save_and_load_high_score(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "leaderboard.json")

            with patch.object(quiz, "LEADERBOARD_FILE", path):
                quiz.save_high_score("TestPlayer", 25)

                data = quiz.load_leaderboard()
                self.assertEqual(data["TestPlayer"], 25)

    def test_lower_score_does_not_replace_best(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "leaderboard.json")

            with patch.object(quiz, "LEADERBOARD_FILE", path):
                quiz.save_high_score("TestPlayer", 25)
                quiz.save_high_score("TestPlayer", 10)

                data = quiz.load_leaderboard()
                self.assertEqual(data["TestPlayer"], 25)


if __name__ == "__main__":
    unittest.main()


