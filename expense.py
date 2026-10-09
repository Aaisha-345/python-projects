import json
import os

# File name for saving/loading data (Level 03 Challenge)
DATA_FILE = "expenses.json"

def load_expenses():
    """Loads expenses from a JSON file if it exists."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "file_mode" == "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(" Warning: Data file was corrupted. Starting with an empty list.")
    return []

def save_expenses(expenses):
    """Saves the expenses list to a JSON file (Level 03 Challenge)."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
    except IOError:
        print("Error: Could not save expenses to file.")

def add_expense(expenses):
    """Adds a new expense dictionary to the list (Level 01 MVP & Level 02 Categories)."""
    name = input("Enter expense name (e.g., Lunch): ").strip()
    if not name:
        print(" Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: $"))
        if amount < 0:
            print(" Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid number. Please enter a valid amount.")
        return

    # Level 02 Feature: Add categories
    print("\nSelect a category:")
    print("1. Food\n2. Travel\n3. Entertainment\n4. Others")
    category_choice = input("Choose (1-4): ").strip()
    
    categories = {"1": "Food", "2": "Travel", "3": "Entertainment", "4": "Others"}
    category = categories.get(category_choice, "Others")

    # Level 01 & 02 dictionary structure
    expense_item = {
        "name": name,
        "amount": amount,
        "category": category
    }
    
    expenses.append(expense_item)
    save_expenses(expenses)
    print(f"Added: {name} (${amount:.2f}) under [{category}]")

def view_expenses(expenses):
    """Displays all recorded expenses (Level 01 MVP)."""
    if not expenses:
        print("\n No expenses recorded yet.")
        return

    print("\n---  All Expenses ---")
    for idx, x in enumerate(expenses, start=1):
        print(f"{idx}. {x['name']} - ${x['amount']:.2f} [{x['category']}]")

def show_total_spent(expenses):
    """Calculates and displays total spent using list comprehension and sum() (Level 01 MVP)."""
    total = sum([x["amount"] for x in expenses])
    print(f"\nTotal Spent: ${total:.2f}")

def find_largest_expense(expenses):
    """Finds and prints the single highest expense (Level 03 Challenge)."""
    if not expenses:
        print("\n No expenses to evaluate.")
        return

    # Use max() with a key function to find the dict with the largest amount
    largest = max(expenses, key=lambda x: x["amount"])
    print(f"\nHighest Expense: {largest['name']} (${largest['amount']:.2f}) [{largest['category']}]")

def main():
    """Interactive CLI loop for the application."""
    expenses = load_expenses()

    while True:
        print("\n=======  Expense Tracker =======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Find Highest Expense")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total_spent(expenses)
        elif choice == "4":
            find_largest_expense(expenses)
        elif choice == "5":
            print(" Goodbye! Your data has been saved safely.")
            break
        else:
            print(" Invalid choice. Please pick an option from 1 to 5.")

if __name__ == "_main_":
    main()