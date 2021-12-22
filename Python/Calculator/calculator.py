# Imports
from functions import *
from art import *
import os


def calculator(continue_operations = True):
    while continue_operations:
        # Clear the screen each time
        os.system("clear")
        # Print the logo each time
        print(f"{logo}")

        # Ask for the first number
        num1 = float(input("What's the first number: "))

        # Display possible operations
        for item in operations:
            print(item)
        # Ask the user to pick an operation
        operation_symbol = input("Pick an operation: ")

        # Ask for the second number
        num2 = float(input("What's the second number: "))

        # operations[operation_symbol] ---> is a function
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        # Print result
        print(f"{num1} {operation_symbol} {num2} = {answer}.")

        # Ask the user if they wish to run the sequence again
        choice = input("Run again (yes, no): ")
        if choice == 'yes':
            calculator()
        else:
            continue_operations = False

# Fisrt function call
calculator()