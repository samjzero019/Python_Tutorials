import sys

# print system version
print("SYSTEM  level python VERSION:", sys.version)

# print python interpreter path
print("path:", sys.executable)

# let make a greeting function with return value

"""
    string interpolation in python is done either by final string  or format function
"""


def greeting(super_admin="HG|Alpha"):
    return (
        f"Attention! Attention! {super_admin} has joined the server! "
        + "Everyone Freeze! for {}".format(super_admin)
    )


name = input("Just Yur Name: ")

print(greeting())
print(greeting(name))
