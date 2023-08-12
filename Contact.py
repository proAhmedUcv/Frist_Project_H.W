contacts = []

def add_contact():
    print("----- Add a Contact -----")
    name = input("Enter the name: ")
    number = input("Enter the number: ")
    contact = {"name": name, "number": number}
    contacts.append(contact)
    print("Contact added successfully.")

def display_contacts():
    print("----- Contacts -----")
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index+1}. Name: {contact['name']}, Number: {contact['number']}")

def edit_contact():
    display_contacts()
    if len(contacts) == 0:
        return

    print("----- Edit a Contact -----")
    index = int(input("Enter the index of the contact to edit: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Invalid index.")
        return

    name = input("Enter the new name: ")
    number = input("Enter the new number: ")
    contacts[index]["name"] = name
    contacts[index]["number"] = number
    print("Contact edited successfully.")

def delete_contact():
    display_contacts()
    if len(contacts) == 0:
        return

    print("----- Delete a Contact -----")
    index = int(input("Enter the index of the contact to delete: ")) - 1
    if index < 0 or index >= len(contacts):
        print("Invalid index.")
        return

    del contacts[index]
    print("Contact deleted successfully.")

def contact_manager():
    print("Welcome to the Contact Manager!")

    while True:
        print("\n----- Menu -----")
        print("1. Add a contact")
        print("2. Display contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you for using the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

contact_manager()