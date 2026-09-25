"""
Contact Book using Dictionary
"""

# Contacts are stored as {name: phone_number}
contacts = {}


def add_contact():
    """Add a new contact to the dictionary."""
    name = input("Enter contact name: ").strip().title()
    if not name:
        print("Name cannot be empty.\n")
        return

    if name in contacts:
        print(f"'{name}' already exists with number {contacts[name]}.")
        print("Use the Update option to change it.\n")
        return

    number = input("Enter phone number: ").strip()
    if not number:
        print("Phone number cannot be empty.\n")
        return

    contacts[name] = number
    print(f"Contact '{name}' added successfully.\n")


def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip().title()
    if name in contacts:
        print(f"Found -> {name}: {contacts[name]}\n")
    else:
        print(f"No contact found with the name '{name}'.\n")


def update_contact():
    """Update the phone number of an existing contact."""
    name = input("Enter name to update: ").strip().title()
    if name not in contacts:
        print(f"No contact found with the name '{name}'.\n")
        return

    new_number = input(f"Enter new number for {name}: ").strip()
    if not new_number:
        print("Phone number cannot be empty.\n")
        return

    contacts[name] = new_number
    print(f"Contact '{name}' updated successfully.\n")


def delete_contact():
    """Delete a contact from the dictionary."""
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print(f"No contact found with the name '{name}'.\n")


def show_all():
    """Display all saved contacts."""
    if not contacts:
        print("Contact book is empty.\n")
        return

    print("\n--- All Contacts ---")
    for name, number in sorted(contacts.items()):
        print(f"{name:<20} {number}")
    print()


def main():
    menu = (
        "\n===== Contact Book =====\n"
        "1. Add Contact\n"
        "2. Search Contact\n"
        "3. Update Contact\n"
        "4. Delete Contact\n"
        "5. Show All Contacts\n"
        "6. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_all()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
