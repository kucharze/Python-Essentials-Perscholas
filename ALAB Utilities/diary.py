import os
import calendar
import datetime

#Check if diary.txt exists, if not create it
if not os.path.exists("diary.txt"):
    with open("diary.txt", "w") as f:
        f.write("Diary created.\n")
        
        
with open("diary.txt", "a") as f:
    entry = input("Enter your diary entry: ")
    f.write(entry + "\n")
    f.write("Diary updated.\n")