"""
CP1404 | Prac_02 | Score Menu

"""
from score import determine_result, get_valid_score
from math import floor

MENU = "(S)tars \n(R)esult \n(Q)uit \n>>> "


def main():
    """Get score, display stars or display result"""
    choice = input(MENU).upper()
    while choice != "Q":
        score = get_valid_score()
        if choice == "S":
            print("*" * floor(score))
        elif choice == "R":
            print(determine_result(score))
        else:
            print("Invalid choice")
        choice = input(MENU).upper()
    print("Finished.")


main()
