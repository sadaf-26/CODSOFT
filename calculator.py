# Simple Calculator in Python

# Function to perform the arithmetic operations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

def main():
    # Prompt user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numerical values.")
        return
    
    # Prompt user to choose an operation
    print("Choose an operation: add, subtract, multiply, divide")
    operation = input("Enter the operation: ").strip().lower()
    
    # Perform calculation and display result
    result = calculate(num1, num2, operation)
    print("The result is:", result)

# Execute the main function
if __name__ == "__main__":
    main()
