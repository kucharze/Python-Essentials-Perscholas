def safe_divide(a, b):
    if b == 0:#Check for division by zero if so raise error
        raise ValueError("Cannot divide by zero.")
    
    result = a / b
    
    return result


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = safe_divide(num1, num2)
    print(num1, "/", num2, "=", result)
except ValueError as e:#Specific exception for value error raised in safe_divide function
    print("Error:", e)
except Exception as e: #Generic exception
    print("An unexpected error occurred:", e)
finally:
    print("Division operation completed!")