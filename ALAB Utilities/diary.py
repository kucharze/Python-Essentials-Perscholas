import os
import datetime

try:
    #Check if diary.txt exists, if not create it
    if not os.path.exists("diary.txt"):
        with open("diary.txt", "w") as f:
            f.write("Diary created.\n")
            
    #Add a new entry to the diary
    with open("diary.txt", "a") as f:
        entry = input("Enter your diary entry: ")
        f.write(str(datetime.datetime.now()) + "\n")
        f.write(entry + "\n")
        f.write("Diary updated.\n")
        
    #Read the contents of the diary
    with open("diary.txt", "r") as f:
        print(f.read())
        
except Exception as e:
    print(f"An error occurred: {e}")