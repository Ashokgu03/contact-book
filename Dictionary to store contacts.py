# Dictionary to store contacts
contacts = {}

def display_menu():
    print("\n=== Simple Contact Book ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Editing contact '{name}'.")
        new_name = input(f"Enter new name (leave empty to keep '{name}'): ")
        new_phone = input(f"Enter new phone number (leave empty to keep '{contacts[name]['phone']}'): ")
        new_email = input(f"Enter new email (leave empty to keep '{contacts[name]['email']}'): ")
        
        # If a new name is provided, update the contact name
        if new_name:
            contacts[new_name] = {
                'phone': new_phone or contacts[name]['phone'],
                'email': new_email or contacts[name]['email']
            }
            del contacts[name]  # Remove the old contact
        else:
            contacts[name] = {
                'phone': new_phone or contacts[name]['phone'], 
                'email': new_email or contacts[name]['email']
            }

        print(f"Contact updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def search_contact():
    query = input("Enter the name or part of the name to search: ")
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
            found = True
    if not found:
        print(f"No contacts found matching '{query}'.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()