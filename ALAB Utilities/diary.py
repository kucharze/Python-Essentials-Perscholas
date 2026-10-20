import os

#Check if diary.txt exists, if not create it
if not os.path.exists("diary.txt"):
    with open("diary.txt", "w") as f:
        f.write("Diary created.\n")
        
        
