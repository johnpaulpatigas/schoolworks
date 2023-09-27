# simpleCalculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
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
    user_input = get_user_input().lower()

    if user_input == "quit":
        break

    if user_input in operations:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = operations[user_input](num1, num2)
            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid input. Please try again.")
