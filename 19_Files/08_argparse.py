import argparse

# Create an ArgumentParser object to handle command-line arguments
parser = argparse.ArgumentParser(description="Simple calculator")

# Add the first number as a positional argument
parser.add_argument("num1", type=float, help="First number")

# Add the second number as a positional argument
parser.add_argument("num2", type=float, help="Second number")

# Add the operation argument with restricted choices
parser.add_argument(
    "operation",
    choices=["add", "sub", "mul", "div"],
    help="Operation to perform"
)

# Parse the command-line arguments and store them in 'args'
args = parser.parse_args()

# Perform addition if operation is 'add'
if args.operation == "add":
    result = args.num1 + args.num2

# Perform subtraction if operation is 'sub'
elif args.operation == "sub":
    result = args.num1 - args.num2

# Perform multiplication if operation is 'mul'
elif args.operation == "mul":
    result = args.num1 * args.num2

# Perform division if operation is 'div'
elif args.operation == "div":
    # Check for division by zero to avoid runtime error
    if args.num2 == 0:
        print("Error: Division by zero is not allowed")
        exit()
    result = args.num1 / args.num2

# Print the final calculated result
print("Result:", result)
