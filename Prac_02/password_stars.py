"""
CP1404 | Prac_02 | Password Stars
Get user password and check length is longer than minimum length.
"""
MINIMUM_LENGTH = 8


def main():
    """Display valid password as stars.."""
    password = get_password()
    print("*" * len(password))


def get_password():
    """Get password and check valid length."""
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error")
        password = input("Password: ")
    return password
