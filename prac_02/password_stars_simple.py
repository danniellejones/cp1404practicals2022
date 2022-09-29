"""
CP1404 | Prac_02 | Password Stars
Get user password and check length is longer than minimum length.
"""
MINIMUM_LENGTH = 8

password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print("Error")
    password = input("Password: ")
print("*" * len(password))
