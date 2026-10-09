# Simple Inventory Manager
# Project 12: Practice dictionaries, lists, and CRUD operations.

# Initialize the inventory dictionary
# Structure: { "product_name": quantity }
inventory = {}

# Threshold for low-stock alert (Challenge feature)
LOW_STOCK_THRESHOLD = 5

def display_menu():
    print("\n--- Inventory Manager Menu ---")
    print("1. Add / Update Product (Create/Update)")
    print("2. View All Products (Read)")
    print("3. Search Product by Name (Read)")
    print("4. Delete Product (Delete)")
    print("5. Check Low-Stock Alerts (Challenge)")
    print("6. Exit")

def add_or_update_product():
    # Strip whitespace and convert to lowercase for consistency
    name = input("Enter product name: ").strip().lower()
    if not name:
        print("Product name cannot be empty.")
        return
    
    try:
        quantity = int(input(f"Enter quantity for '{name}': "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
            
        # Add or update the dictionary key-value pair
        inventory[name] = quantity
        print(f"Success: '{name}' is now set to {quantity}.")
    except ValueError:
        print("Invalid input! Quantity must be a whole number.")

def view_all_products():
    if not inventory:
        print("The inventory is currently empty.")
        return
        
    print("\n--- Current Inventory ---")
    for name, quantity in inventory.items():
        print(f"- {name.capitalize()}: {quantity} units")

def search_product():
    name = input("Enter the product name to search: ").strip().lower()
    
    # Handle missing items safely using 'in' operator
    if name in inventory:
        print(f"Found: '{name.capitalize()}' has {inventory[name]} units in stock.")
    else:
        print(f"Error: '{name.capitalize()}' is not in the inventory.")

def delete_product():
    name = input("Enter the product name to delete: ").strip().lower()
    
    # Check existence before deleting to handle missing items safely
    if name in inventory:
        del inventory[name]
        print(f"Success: '{name.capitalize()}' has been removed from inventory.")
    else:
        print(f"Error: '{name.capitalize()}' not found. Cannot delete.")

def check_low_stock():
    print(f"\n--- Low Stock Alerts (Under {LOW_STOCK_THRESHOLD} units) ---")
    low_stock_items = [name for name, qty in inventory.items() if qty < LOW_STOCK_THRESHOLD]
    
    if not low_stock_items:
        print("All products are well stocked!")
    else:
        for name in low_stock_items:
            print(f"ALERT: '{name.capitalize()}' is low on stock ({inventory[name]} left)!")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == "1":
            add_or_update_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            check_low_stock()
        elif choice == "6":
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()