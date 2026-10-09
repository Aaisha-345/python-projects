import json
import os

# File name for Level 03 challenge (JSON storage)
DATA_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from a JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(" Data file corrupted. Starting with an empty contact book.")
            return []
    return []

def save_contacts(contacts):
    """Saves the current contact list to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Level 01: Saves contact name & phone as a dictionary."""
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    
    phone = input("Enter phone number: ").strip()
    
    # Create contact dictionary structure
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    
    save_contacts(contacts)  # Save progress
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    """Level 01: Displays all saved contacts."""
    if not contacts:
        print(" Your contact book is empty.")
        return

    print("\n--- Saved Contacts ---")
    for index, contact in enumerate(contacts, 1):
        print(f"{index}. Name: {contact['name']} | Phone: {contact['phone']}")
    print("-" * 22)

def search_contact(contacts):
    """Level 02: Finds and displays contact by name (case-insensitive)."""
    if not contacts:
        print(" Your contact book is empty.")
        return

    query = input("Enter the name to search for: ").strip().lower()
    found = False

    print("\n--- Search Results ---")
    for contact in contacts:
        # Case-insensitive partial or exact matching
        if query in contact["name"].lower():
            print(f" Found -> Name: {contact['name']} | Phone: {contact['phone']}")
            found = True
            
    if not found:
        print("No matching contacts found.")
    print("-" * 22)

def delete_contact(contacts):
    """Level 02: Removes a contact entry by name."""
    if not contacts:
        print(" Your contact book is empty.")
        return

    name_to_delete = input("Enter the exact name of the contact to delete: ").strip()
    
    # Search and filter out the match
    initial_length = len(contacts)
    contacts[:] = [c for c in contacts if c["name"].lower() != name_to_delete.lower()]

    if len(contacts) < initial_length:
        save_contacts(contacts)  # Save updated list
        print(f" Contact '{name_to_delete}' has been deleted.")
    else:
        print(f" Contact '{name_to_delete}' not found.")

def main():
    # Initialize list of dicts structure from saved file
    contacts = load_contacts()

    while True:
        print("\n --- CONTACT BOOK MENU ---")
        print("1. Add Contact (MVP)")
        print("2. View Contacts (MVP)")
        print("3. Search Contact (Improvement)")
        print("4. Delete Contact (Improvement)")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print(" Exiting Contact Book. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()