"""
Kelly Sturdevant
Final Project for 2025 Spring Semester Python 2 (CIS256 13732)

Jotto is a simple word guessing game
(modeled after https://en.wikipedia.org/wiki/Jotto)
"""


def get_menu_selection():
    menu_selection = 0

    while menu_selection < 1 or menu_selection > 4:
        print("\nWelcome to Jotto!")
        print("1. Start a new game")
        print("2. View the rules of Jotto")
        print("3. See an example game")
        print("4. Exit")
        menu_selection = int(
            input("What would you like to do? Enter the number here: ")
        )

    return menu_selection


match get_menu_selection():
    case 1:
        print("Ok, let's start a new game")
    case 2:
        print("Here are the rules:")
    case 3:
        print("Here's an example game")
    case _:
        print("Goodbye!")
