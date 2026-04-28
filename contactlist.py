contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added")

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Not found")

    elif choice == "5":
        break