import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()

    if not phone.isdigit():
        print("Invalid phone number.")
        return

    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    name = input("Enter Name to Search: ").strip()
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter Name to Update: ").strip()
    if name in contacts:
        new_phone = input("Enter New Phone: ").strip()
        if new_phone.isdigit():
            contacts[name] = new_phone
            save_contacts(contacts)
            print("Contact updated.")
        else:
            print("Invalid phone number.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter Name to Delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

def show_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            show_all_contacts(contacts)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
