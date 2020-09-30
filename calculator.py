"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    #until 'q' is entered
    user_input = input("Enter your equation > ")
    token = user_input.split(' ')

    if tokens < 2:
        print("Error, please enter math type and two numbers")

    if user_input = 'q':
        break

