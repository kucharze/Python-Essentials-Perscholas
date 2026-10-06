grade = input("Enter your grade: ")
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#0-59: F

if grade >= "90":
    print("Your grade is: A")
elif grade >= "80":
    print("Your grade is: B")
elif grade >= "70":
    print("Your grade is: C")
elif grade >= "60":
    print("Your grade is: D")
else:
    print("Your grade is: F")
    
if grade >= "70":
    print("You passed the class!")
else:
    print("You did not pass the class! Better luck next time.")