"""
Kelly Sturdevant
Final Project for 2025 Spring Semester Python 2 (CIS256 13732)

Jotto is a simple word guessing game
(modeled after https://en.wikipedia.org/wiki/Jotto)
"""

from jotto_game import JottoGame


def get_menu_selection():
    menu_selection = 0

    while menu_selection < 1 or menu_selection > 5:
        print("\nWelcome to Jotto!\n")
        print("1. Start a new game")
        print("2. View the rules of Jotto")
        print("3. See a list of valid words")
        print("4. Exit")
        menu_selection = int(
            input("\nWhat would you like to do? Enter the number here: ")
        )

    return menu_selection


def play_a_game():
    game = JottoGame()
    print("\nOk, let's start a new game\n")
    while game.get_status() != "Won":
        print(game.add_guess(input("Enter a guess word here: ")))


def print_rules():
    rules = (
        "\nJotto is a deductive word game with the purpose of correctly guessing a 5 letter word. The secret word is a valid scrabble word, and no proper nouns are allowed.\n"
        "The player submits valid 5 letter words as guesses, and the game returns the number of letters from the guess word that match a letter in the secret word. This number of matching letters is called the jots.\n"
        "For example, if the secret word is 'games', and the guess word is 'soggy', then there are 2 jots, one for the matching 'g', and one for the matching 's'.\n"
        "For another example, if the secret word is 'apple', and the guess word is 'peels', then there are 2 jots, one for the matching 'p', and one for the matching 'e'.\n"
        "When the secret word is correctly guessed, that's Jotto!\n\n"
        "Learn more about Jotto on Wikipedia (https://en.wikipedia.org/wiki/Jotto).\n\n"
    )
    print(rules)


def print_valid_words():
    game = JottoGame()
    starting_letter = ""
    while starting_letter != "0":
        starting_letter = input("\nEnter a starting letter here (Enter 0 to exit): ")
        print()
        for word in game.get_valid_words():
            if word["word"][0] == starting_letter:
                print(f"{word['word']}, ", end="")
        print()


match get_menu_selection():
    case 1:
        play_a_game()
    case 2:
        print_rules()
    case 3:
        print_valid_words()
    case _:
        print("Goodbye!")
