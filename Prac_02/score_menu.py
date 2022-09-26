"""
CP1404 | Prac_02 | Score Menu
Get a valid score and either print stars * score or determine result of score.
"""
from score import determine_result, get_valid_score

MENU = "(S)tars \n(R)esult \n(Q)uit \n>>> "


def main():
    """Get score, display stars or display result"""
    choice = input(MENU).upper()
    while choice != "Q":
        score = get_valid_score()  # This could be an option to change score
        if choice == "S":
            print("*" * int(score))  # If password_stars uses print_star function import and re-use that function here
        elif choice == "R":
            print(determine_result(score))
        else:
            print("Invalid choice")
        choice = input(MENU).upper()
    print("Finished.")


main()
