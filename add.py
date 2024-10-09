# Simple addition and subtraction calculator

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose the operation
operation = input("Choose operation (+ for add, - for subtract): ")

# Perform the operation
if operation == '+':
    print(f"The result is: {num1 + num2}")
elif operation == '-':
    print(f"The result is: {num1 - num2}")
else:
    print("Invalid operation!")
