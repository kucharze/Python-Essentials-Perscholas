months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#The first and last month
print(months[0])  # January
print(months[-1])  # December

try:
    #Trying to change a value in the tuple
    months[0] = "Jan"
except TypeError as e:
    print("Cannot modify tuples. Error:", e)  # 'tuple' object does not support item assignment