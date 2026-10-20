import calendar
import datetime

year = int(input("Enter the year: "))
month = int(input("Enter a number for the month: "))

print("")
print("Calendar for", calendar.month_name[month], year)
print(calendar.month(year, month))
print("")

#Print out the current date
current_date = datetime.datetime.now()
print("Current date and time: ", current_date)

#Check if the current year and month match the user input
if current_date.year == year and current_date.month == month:
    print("The current month and year match the user input.")