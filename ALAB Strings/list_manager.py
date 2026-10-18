nums = [2,4,67,23,11,90,34,56,78,123,5,6,7,8,9,10]

while True:
    print("Choose an option:")
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Display numbers")
    print("4. Exit")
    
    
    
    try:
        option = input("Enter your choice: ")
        
        if option == "1":
            num = int(input("Enter a number: "))
            nums.append(num)
            
        elif option == "2":
            num = int(input("Enter a list position: "))
            if 0 <= num < len(nums):
                nums.pop(num)
            else:
                print("Index out of range.")
                raise IndexError("Index out of range.")
                
        elif option == "3":
            print("")
            print("Numbers in the list:")
            for n in nums:
                print(n, end = " ")
            print("")  # Print a newline after displaying all numbers

        elif option == "4":
            break
        else:
            print("Invalid option. Please try again.")
            
    except IndexError: #Error for index out of range
        print("Index out of range. Please try again.")
        
    except ValueError: #Error for invalid input
        print("Invalid input. Please enter a valid number.")