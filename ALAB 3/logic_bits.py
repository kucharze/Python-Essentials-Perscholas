print("Input two boolean inputs (True or False) to see the results of logical operations.")
b1 = input("Enter first boolean input: ")
b2 = input("Enter second boolean input: ")

print("b1 and b2:", b1 and b2)
print("b1 or b2:", b1 or b2)
print("not b1:", not b1)

print("Demonstrating bitwise operations on integers.")
x = int(input("Enter the first integer: "))
y = int(input("Enter the second integer: "))
#bin function is used to convert an integer to its binary representation
print("x & y:", bin(x & y))
print("x | y:", bin(x | y))
print("x ^ y:", bin(x ^ y))
print("~x:", bin(~x))
print("x << 2:", bin(x << 2))
print("x >> 2:", bin(x >> 2))