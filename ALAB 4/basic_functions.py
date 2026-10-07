def greet_user(name):
    #Greets the user with their name
    print("Hello,", name + "! Welcome!")
    
def add_two_numbers(a, b):
    #Adds two numbers and returns the result
    return a + b

def is_even(num):
    #Checks if a number is even and returns a boolean value
    if num % 2 == 0:
        return True
    else:
        return False
    

#All function calls
greet_user("Zachary")
sum = add_two_numbers(5, 10)
print("The sum of 5 and 10 is:", sum)
print("2 + 3 =", add_two_numbers(2, 3))

b1 = is_even(5)
b2 = is_even(6)
print("5 is even:", b1)
print("6 is even:", b2)