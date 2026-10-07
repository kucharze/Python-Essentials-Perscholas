contacts = {
    "Zachary": ["123-456-7890"],
    "John": ["987-654-3210"],
    "Jane": ["555-555-5555"]
}

def add_contact(name, phone_number):
    if name in contacts:
        contacts[name].append(phone_number)
    else:
        contacts[name] = [phone_number]


#Contact Book Menu:
#1. Add New Contact
#2. View All Contacts
#3. Search Contact
#4. Delete Contact
#5. Exit
#Enter your choice (1-5):

while True:
    print("Contact Book Menu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    
    if choice == "1":
        print("Add New Contact:")
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == "2":
        print("All Contacts:")
        for name in contacts.items():
            print(name, ": ", contacts[name])
    elif choice == "3":
        print("Search Contact:")
        pass
    elif choice == "4":
        print("Delete Contact:")
        pass
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break