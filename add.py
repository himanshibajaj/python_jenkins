import sys

# Check if enough arguments are provided
if len(sys.argv) != 4:
    print("Usage: python add.py <num1> <num2> <operation>")
    sys.exit(1)

# Get numbers and operation from command-line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

# Perform calculation based on the operation
if operation == '+':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
else:
    print("Invalid operation!")
