"""
CP1404 | Prac_02 | Score
Program to determine result based on score.
"""
from random import randint


def main():
    """Get score and display result"""
    score = get_valid_score()
    result = determine_result(score)
    print(f"Score: {score} Result: {result}")
    # Use a random integer score
    score = randint(0, 100)
    result = determine_result(score)
    print(f"Score: {score} Result: {result}")


def get_valid_score():
    """Get valid score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """Determine result of score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":  # Allows import of function into another program without running main()
    main()
