def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    
    result = a / b
    
    return result


try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    result = safe_divide(num1, num2)
    print(num1, "/", num2, "=", result)
except ValueError as e:
    print("Error:", e)
finally:
    print("Division operation completed!")