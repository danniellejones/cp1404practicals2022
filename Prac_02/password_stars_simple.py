"""
CP1404 | Prac_02 | Password Stars
Get user password and check length is longer than minimum length.
"""

password = input("Password: ")
minimum_length = 8
while len(password) < minimum_length:
    print("Error")
    password = input("Password: ")
print("*" * len(password))
