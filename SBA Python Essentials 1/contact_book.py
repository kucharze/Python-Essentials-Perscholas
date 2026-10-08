contacts = {
    "Zachary": 1234567890,
    "John": 9876543210,
    "Jane": 5555555555
}

def add_contact(name, phone_number):#Add a new contact to the contacts dictionary
    if name in contacts:
        #No duplicate entries, print an error
        print("Contact already exists.")
    else:
        contacts[name] = phone_number
        
        
def view_contacts():#View all contacts in the contacts dictionary
    for name, phone_number in contacts.items():
        print(name, ": ", phone_number)
        
        
def search_contact(name):#Search for a contact by name
    if name in contacts:
        return contacts[name]
    else:
        return None
    

def delete_contact(name):#Delete a contact from the contacts dictionary
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found.")


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
    
    try:
        if choice == "1":
            print("Add New Contact:")
            name = input("Enter contact name: ")
            phone_number = int(input("Enter phone number: "))
            add_contact(name, phone_number)
        elif choice == "2":
            print("All Contacts:")
            view_contacts()
                
        elif choice == "3":
            print("Search Contact:")
            name = input("Enter contact name: ")
            phone_number = search_contact(name)
            if phone_number:
                print(name, ": ", phone_number)
            else:
                print("Contact not found.")
                
        elif choice == "4":
            print("Delete Contact:")
            name = input("Enter contact name: ")
            delete_contact(name)
                
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input option received.")
    except Exception as e:
        print("An unexpected error occurred:", e)