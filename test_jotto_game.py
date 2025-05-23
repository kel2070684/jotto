"""
This is a suite of test cases for jotto_game.py
"""

import unittest
from jotto_game import *


class TestJottoGame(unittest.TestCase):

    def setUp(self):
        self.game_aaaaa = JottoGame("aaaaa")
        self.game_exist = JottoGame("exist")

    def test_get_status_started(self):
        self.assertEqual(self.game_aaaaa.get_status(), "Started")
        self.assertEqual(self.game_exist.get_status(), "Started")

    def test_select_secret_word(self):
        game_01 = JottoGame()
        self.assertNotEqual(game_01.select_secret_word(), game_01.select_secret_word())

    def test_calculate_jots(self):
        self.assertEqual(self.game_aaaaa.calculate_jots("exist"), 0)
        self.assertEqual(self.game_aaaaa.calculate_jots("axxxx"), 1)
        self.assertEqual(self.game_aaaaa.calculate_jots("axaxx"), 2)
        self.assertEqual(self.game_aaaaa.calculate_jots("axxaa"), 3)
        self.assertEqual(self.game_aaaaa.calculate_jots("xaaaa"), 4)
        self.assertEqual(self.game_aaaaa.calculate_jots("aaaaa"), 5)

        self.assertEqual(self.game_exist.calculate_jots("aaaaa"), 0)
        self.assertEqual(self.game_exist.calculate_jots("saaaa"), 1)
        self.assertEqual(self.game_exist.calculate_jots("sxaaa"), 2)
        self.assertEqual(self.game_exist.calculate_jots("tsiaa"), 3)
        self.assertEqual(self.game_exist.calculate_jots("state"), 3)
        self.assertEqual(self.game_exist.calculate_jots("tsixa"), 4)
        self.assertEqual(self.game_exist.calculate_jots("exits"), 5)
        self.assertEqual(self.game_exist.calculate_jots("exist"), 5)

    def test_is_guess_word_valid(self):
        self.assertEqual(self.game_exist.is_guess_word_valid("exist"), True)
        self.assertEqual(self.game_exist.is_guess_word_valid("aaaaa"), False)

    def test_add_guess(self):
        self.assertEqual(self.game_exist.add_guess("aaaaa"), "guess is invalid")
        self.assertEqual(self.game_exist.add_guess("blame"), "Blame is 1 jots!")
        self.assertEqual(self.game_exist.add_guess("stump"), "Stump is 2 jots!")
        self.assertEqual(self.game_exist.add_guess("axels"), "Axels is 3 jots!")
        self.assertEqual(self.game_exist.add_guess("tries"), "Tries is 4 jots!")
        self.assertEqual(self.game_exist.add_guess("exits"), "Exits is 5 jots!")
        self.assertEqual(
            self.game_exist.add_guess("exist"),
            "\n\t Jotto! Exist is the secret word!\n",
        )

    def test_get_status_won(self):
        self.game_exist.add_guess("exist")
        self.assertEqual(self.game_exist.get_status(), "Won")

    def test_is_guess_word_valid(self):
        self.assertEqual(self.game_exist.is_guess_word_valid("snake"), True)
        self.assertEqual(self.game_exist.is_guess_word_valid("aaaaa"), False)


if __name__ == "__main__":
    unittest.main()
