"""
Kelly Sturdevant
Final Project for 2025 Spring Semester Python 2 (CIS256 13732)

Jotto is a simple word guessing game
(modeled after https://en.wikipedia.org/wiki/Jotto)
"""

from random import randint
import csv


class JottoGame:
    def __init__(self, secret_word):
        self.guesses = []
        self.status = "Started"
        self.valid_words = self.get_valid_words(5)

        if secret_word:
            self.__secret_word = {"word": secret_word, "definition": "test"}
        else:
            self.__secret_word = self.select_secret_word(5)

    def print_game_info(self):
        print(f"\nGame status: {self.status}")
        print(f"Number of guesses: {len(self.guesses)}\n")
        for guess in self.guesses:
            print(f"\tGuess: {guess['word']}\t Jots: {guess['jots']}")

    def get_status(self):
        return self.status

    def get_valid_words(self, word_length):
        valid_words = []

        with open("scrabble_words.txt", newline="") as scrabble_words:
            word_reader = csv.DictReader(
                scrabble_words, delimiter="\t", fieldnames=["word", "definition"]
            )
            for line in word_reader:
                if len(line["word"]) == word_length:
                    valid_words.append(
                        {"word": line["word"].lower(), "definition": line["definition"]}
                    )

    def select_secret_word(self):
        return self.valid_words(randint(0, len(self.valid_words) - 1))

    def add_guess(self, guess_word):
        guess_word = guess_word.lower()
        if self.is_guess_word_valid(guess_word):
            isJotto = False
            jots = 0

            if self.__secret_word["word"] == guess_word:
                jots = 5
                isJotto = True
                self.status = "Won"
            else:
                jots = self.calculate_jots(guess_word)

            self.guesses.append({"Guess": guess_word, "Jots": jots, "Jotto": isJotto})
            return f"{self.guesses[-1]["jots"]} jots!"
        else:
            return "guess is invalid"

    def is_guess_word_valid(self, guess_word):
        return guess_word.lower() in self.valid_words

    def calculate_jots(self, guess_word):
        jots = 0
        guess_word = guess_word.lower()

        for letter in guess_word:
            for character in self.__secret_word["word"]:
                if letter == character:
                    jots += 1
                    character = "!"
                    letter = "@"

        return jots
