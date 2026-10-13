import math
import random
import platform

#Generate a random number between 0 and 100
rand = random.uniform(0, 100)
print("Random number between 0 and 100: ")
print(rand)


#Calculate the square root of the random number
sqrt = math.floor(math.sqrt(rand))
print("Square root of the random number: ")
print(sqrt)

#Print out OS name and Python version
print("OS Name: ")
print(platform.system())
print(platform.python_version())