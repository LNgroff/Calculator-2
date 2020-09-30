"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# token = [+, 3, 4]
# Replace this with your code
while True:
    #until 'q' is entered
    user_input = input("Enter your equation > ")
    token = user_input.split(' ')

    if len(token) < 2:
        print("Error, please enter math type and two numbers")
        continue

    if user_input == 'q':
        break

    operator = token[0]
    num1 = int(token[1])
    num2 = int(token[2])

    elif operator == '+':
         num1 + num2
    
    elif operator == '-':
        print(num1 - num2)
   
    elif operator == '*':
        print(num1 * num2) 
   
    elif operator == '/':
        print(num1 / num2)
   
    elif operator == '**':
        print(num1**2)
    
        

       