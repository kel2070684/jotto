"""
Kelly Sturdevant
Final Project for 2025 Spring Semester Python 2 (CIS256 13732)

Jotto is a simple word guessing game
(modeled after https://en.wikipedia.org/wiki/Jotto)
"""

from random import randint
import csv
from collections import Counter


class JottoGame:
    def __init__(self, secret_word=None):
        self.guesses = []
        self.status = "Started"
        self.valid_words = self.import_valid_scrabble_words()

        if secret_word:
            self.__secret_word = {"word": secret_word, "definition": "test"}
        else:
            self.__secret_word = self.select_secret_word()

    def print_game_info(self):
        print(f"\nGame status: {self.status}")
        print(f"Number of guesses: {len(self.guesses)}")
        for guess in self.guesses:
            print(f"\tGuess: {guess['guess']}\t Jots: {guess['jots']}")

    def get_status(self):
        return self.status

    def get_valid_words(self):
        return self.valid_words

    def import_valid_scrabble_words(self):
        valid_words = []

        # scrabble_words.txt by Collins Scrabble Words (2019) - http://drive.google.com/file/d/1XIFdZukAcDRiDIOgR_rHpICrrgJbLBxV/view
        with open("scrabble_words.txt", newline="") as scrabble_words:
            word_reader = csv.DictReader(
                scrabble_words, delimiter="\t", fieldnames=["word", "definition"]
            )
            for line in word_reader:
                if len(line["word"]) == 5:
                    valid_words.append(
                        {"word": line["word"].lower(), "definition": line["definition"]}
                    )
        return valid_words

    def select_secret_word(self):
        return self.valid_words[randint(0, len(self.valid_words) - 1)]

    def add_guess(self, guess_word):
        guess_word = guess_word.lower()
        isJotto = False
        jots = 0
        result = ""

        if not self.is_guess_word_valid(guess_word):
            result = "guess is invalid"
        else:
            if self.__secret_word["word"] != guess_word:
                jots = self.calculate_jots(guess_word)
                result = f"{guess_word.title()} is {jots} jots!"
            else:
                jots = 5
                isJotto = True
                self.status = "Won"
                result = f"\n\t Jotto! {guess_word.title()} is the secret word!\n"

            self.guesses.append({"guess": guess_word, "jots": jots, "Jotto": isJotto})

        return result

    def is_guess_word_valid(self, guess_word):
        for word in self.valid_words:
            if guess_word == word["word"]:
                return True

        return False

    def calculate_jots(self, guess_word):
        guess_letters = Counter(guess_word.lower())
        target_letters = Counter(self.__secret_word["word"])

        return (guess_letters & target_letters).total()
