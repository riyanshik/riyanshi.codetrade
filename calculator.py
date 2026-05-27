# Simple calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

# Dictionary of functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

if operation in operations:

    result = operations[operation](num1, num2)
    print("Result =", result)

else:
    print("Invalid operation")