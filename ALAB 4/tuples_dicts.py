months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#The first and last month
print(months[0])  # January
print(months[-1])  # December

try:
    #Trying to change a value in the tuple
    months[0] = "Jan"
except TypeError as e:
    print("Cannot modify tuples. Error:", e)  # 'tuple' object does not support item assignment
    
print("")#Used to break up the output for better readability

#Dictionary of students and their grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

#Add a new name
students["Frank"] = 90

print(students)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95, 'Eve': 88, 'Frank': 90}