nums = [2,4,67,23,11,90,34,56,78,123,5,6,7,8,9,10]

while true:
    print("Choose an option:")
    print("1. Add a number")
    print("2. Remove a number")
    print("3. Display numbers")
    print("4. Exit")
    
    option = input("Enter your choice: ")
    
    if option == "1":
        num = int(input("Enter a number: "))
        nums.append(num)
    elif option == "2":
        num = int(input("Enter a number: "))
        if num in nums:
            nums.remove(num)
        else:
            print("Number not found.")
    elif option == "3":
        print("Numbers in the list:")
        for n in nums:
            print(n)
    elif option == "4":
        break
    else:
        print("Invalid option. Please try again.")