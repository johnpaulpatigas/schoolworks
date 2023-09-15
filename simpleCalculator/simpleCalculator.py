# simpleCalculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def display_menu():
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

def get_user_input():
    return input(": ")

operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

while True:
    display_menu()
    user_input = get_user_input()

    if user_input == "quit":
        break

    if user_input in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "divide" and num2 == 0:
            print("Division by zero is not allowed")
        else:
            result = operations[user_input](num1, num2)
            print("Result:", result)
    else:
        print("Invalid input. Please try again.")
