def greet_user(name):
    print("Hello,", name + "! Welcome!")
    
def add_two_numbers(a, b):
    return a + b

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

greet_user("Zachary")
print("2 + 3 =", add_two_numbers(2, 3))
print("5 is even:", is_even(5))
print("6 is even:", is_even(6))