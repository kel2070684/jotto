"""
This is a suite of test cases for jotto_game.py
"""

import unittest
from jotto_game import *


class TestJottoGame(unittest.TestCase):

    def setUp(self):
        self.game_aaaaa = JottoGame("aaaaa")
        self.game_exist = JottoGame("exist")

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
        self.assertEqual(self.game_exist.calculate_jots("tsixa"), 4)
        self.assertEqual(self.game_exist.calculate_jots("exits"), 5)
        self.assertEqual(self.game_exist.calculate_jots("exist"), 5)


if __name__ == "__main__":
    unittest.main()
