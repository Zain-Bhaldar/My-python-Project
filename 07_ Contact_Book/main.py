'''
Contact Book Application
'''
contacts = []
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contact:
        print("No contacts found.")
        return
    print("Contacts List:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_name = input("Enter the name of the contact to search: ").lower()
    found_contacts = [contact for contact in contacts if search_name in contact['name'].lower()]
    if found_contacts:
        print("Found Contacts:")
        for index, contact in enumerate(found_contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")

def edit_contact():
    search_name = input("Enter the name of the contact to edit: ").lower()
    found_contacts = [contact for contact in contacts if search_name in contact['name'].lower()]
    if found_contacts:
        print("Found Contacts:")
        for index, contact in enumerate(found_contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        choice = input("Enter the number of the contact to edit: ")
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            index = int(choice) - 1
            contact = found_contacts[index]
            print(f"Editing contact: {contact['name']}")
            contact['name'] = input("Enter new name (or press Enter to keep current): ") or contact['name']
            contact['phone'] = input("Enter new phone number (or press Enter to keep current): ") or contact['phone']
            contact['email'] = input("Enter new email (or press Enter to keep current): ") or contact['email']
            print(f"Contact {contact['name']} updated successfully!")
        else:
            print("Invalid choice.")
    else:
        print("No contacts found.")

def delete_contact():
    search_name = input("Enter the name of the contact to delete: ").lower()
    found_contacts = [contact for contact in contacts if search_name in contact['name'].lower()]
    if found_contacts:
        print("Found Contacts:")
        for index, contact in enumerate(found_contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        choice = input("Enter the number of the contact to delete: ")
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            index = int(choice) - 1
            contact = found_contacts[index]
            contacts.remove(contact)
            print(f"Contact {contact['name']} deleted successfully!")
        else:
            print("Invalid choice.")
    else:
        print("No contacts found.")

def menu():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()