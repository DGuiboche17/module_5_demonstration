"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.
"""
### description args returns raises

def greet()->None:
    """
    Prints a hello world message.
    """
    print("Hello World!")

def greet_name_age(name: str, age: int) -> None:
    """
    Prints a greeting including name and age.

    Args:
        name (str): The name of the person being greeted.
        age (int): The age of the person being greeted.
    """
    print(f"hello {name} you are {age} years old.")

def math_operations(operand1: int, 
                    operand2: int,
                    operation: str = "+")-> float:
    """
    Returns the result of the addition or subtraction
    math operation. Defaults to addition if an operation is not
    provided.

    Args:
        operand1 (int): Left operand.
        operand2 (int): Right Operand.
        Operation (str): Default = "+" 
                        Symbol representing the math operation.

    Returns:
        float: Result of the math operation.

    Raises:
    ValueError: When operation is not + or -.
    """
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid Operation")
    return float(result)

# Avoid placing multiple statements into
# a try/except if it is not necessary
# try:
#     print(math_operations(1, 3, "+"))
#     print(math_operations(4, 6, "-"))
#     print(math_operations(10, 10, "*"))
# except ValueError as E:
#     print(E)

try:
    print(math_operations(1, 3, "+"))
except ValueError as E:
    print(E)

try:
    print(math_operations(4, 6, "-"))
except ValueError as E:
    print(E)

try:
    print(math_operations(10, 10, "*"))
except ValueError as E:
    print(E)

try:
    print(math_operations(55, 88))
except ValueError as E:
    print(E)

# print(math_operations.__doc__)

# print(help(math_operations))






# greet()
# greet()
# greet_name_age("Dennis", 29)

