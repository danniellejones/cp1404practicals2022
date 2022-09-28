"""
CP1404 | Prac_02 | Password Stars
Get valid password and display password length as number of stars.
Use function for get valid password.
"""
MINIMUM_LENGTH = 8


def main():
    """Display valid password as stars"""
    password = get_valid_password("Password: ", "Not valid", MINIMUM_LENGTH)
    print("*" * len(password))


def get_valid_password(prompt, error_message, minimum):
    """Get password and check valid length"""
    password = input(prompt)
    while len(password) < minimum:
        print(error_message)
        password = input(prompt)
    return password


main()
