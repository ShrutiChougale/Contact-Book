contacts = {}

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter name: ")
        print("Phone:", contacts.get(name, "Not Found"))
    elif choice == "3":
        break
