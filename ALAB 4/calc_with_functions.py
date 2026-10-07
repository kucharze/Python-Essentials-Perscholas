def add(a, b):
    #Adds two numbers and returns the result
    return a + b

def subtract(a, b):
    #Subtracts the second number from the first and returns the result
    return a - b

def multiply(a, b):
    #Multiplies two numbers and returns the result
    return a * b

def divide(a, b):
    #Divides the first number by the second and returns the result
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculate(a, b, operation):
    #Performs the specified operation on two numbers and returns the result
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Error: Invalid operation. Please use +, -, *, or /."
    
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

result = calculate(num1, num2, operation)

print(num1, operation, num2, "=", result)
