import math
def calculate(operation, number):
    if operation == "+":
# Add the number to itself and return the result
        result = number + number
        return result
    elif operation == "-":
# Subtract the number from itself and return the result
        result = number - number
        return result
    elif operation == "*":
# Multiply the number by itself and return the result
        result = number * number
        return result
    elif operation == "/":
# Divide the number by itself and return the result
        result = number / number
        return result
    elif operation == "sqrt":
# Calculate the square root of the number and return the result
        result = math.sqrt(number)
        return result
    else:
# Return an error message if the operation is not recognized
        return "Invalid operation"
operation = input("Enter an operation (+, -, *, /, sqrt): ")
number = input("Enter a number: ")
number = float(number)
result = calculate(operation, number)
print("Result:", result)