"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# token = [+, 3, 4]
# Replace this with your code
while True:
    #until 'q' is entered
    user_input = input("Enter your equation > ")
    tokens = user_input.split(' ')
    
    if user_input == 'q':
        break
    
    elif len(tokens) < 2:
        print("Error, not enough inputs.")
        continue

    operator = token[0]
    num1 = token[1]
    
    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 =token[2]    

    if len(tokens) > 3:
        num3 = token[3]

     result = None   

    if operator == '+':
        result = add(num1, num2)
    
    if operator == '-':
        result = subtract(num1, num2)
   
    if operator == '*':
        result = multiply(num1, num2)
   
    if operator == '/':
        result =  divide(num1, num2)
   
    if operator == '**':
        result = square(num1)
    
        

       