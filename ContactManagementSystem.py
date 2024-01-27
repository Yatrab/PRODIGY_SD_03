import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email address of the contact: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']}: {contact['phone']}, {contact['email']}")

def edit_contact():
    view_contacts()
    if not contacts:
        return

    index = int(input("Enter the index of the contact you want to edit: ")) - 1

    if index < 0 or index >= len(contacts):
        print("Invalid contact index.")
        return

    contact = contacts[index]
    print(f"Editing contact: {contact['name']}")
    new_name = input("Enter the new name (leave empty to keep current): ")
    new_phone = input("Enter the new phone number (leave empty to keep current): ")
    new_email = input("Enter the new email address (leave empty to keep current): ")

    if new_name:
        contact['name'] = new_name
    if new_phone:
        contact['phone'] = new_phone
    if new_email:
        contact['email'] = new_email

    save_contacts(contacts)
    print("Contact edited successfully.")

def delete_contact():
    view_contacts()
    if not contacts:
        return

    index = int(input("Enter the index of the contact you want to delete: ")) - 1

    if index < 0 or index >= len(contacts):
        print("Invalid contact index.")
        return

    contact = contacts[index]
    print(f"Deleting contact: {contact['name']}")
    confirmation = input("Are you sure you want to delete this contact? (yes/no): ")

    if confirmation.lower() == "yes":
        del contacts[index]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact deletion canceled.")

def contact_manager():
    global contacts
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Thank you for using the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact manager program
contact_manager()