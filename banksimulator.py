# --- Core Variables ---
balance = 1000  # Initial starting balance
transaction_history = ["Initial balance: $1000"]
USER_PIN = "1234"  # Simple PIN security challenge


# --- Core Functions ---

def check_balance():
    """Displays the current account balance."""
    print(f"\n Current Balance: ${balance}")


def deposit(amt):
    """Validates and deposits money into the account."""
    global balance
    if amt <= 0:
        print(" Error: Deposit amount must be greater than zero.")
        return False
    
    balance += amt
    log_msg = f"Deposited: ${amt}"
    transaction_history.append(log_msg)
    print(f"Successfully deposited ${amt}.")
    return True


def withdraw(amt):
    """Validates, checks for overdrafts, and withdraws money."""
    global balance
    if amt <= 0:
        print(" Error: Withdrawal amount must be greater than zero.")
        return False
    
    # Progression Level 02: Prevent withdrawals larger than current balance
    if amt > balance:
        print(f" Error: Insufficient funds! Your balance is only ${balance}.")
        return False
        
    balance -= amt
    log_msg = f"Withdrew: ${amt}"
    transaction_history.append(log_msg)
    print(f" Successfully withdrew ${amt}.")
    return True


def show_history():
    """Displays all past transactions."""
    print("\nTransaction History:")
    for transaction in transaction_history:
        print(f" - {transaction}")


# --- Main CLI Application Loop ---

def main():
    print("=================================")
    print("   WELCOME TO COSMOS CLI BANK   ")
    print("=================================")
    
    # Challenge Level: Simple PIN Security
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN to login: ")
        if entered_pin == USER_PIN:
            print("\n Access Granted!")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
            if attempts == 0:
                print(" Account locked. Goodbye!")
                return

    # Main Interactive Menu
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            check_balance()
            
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                deposit(amount)
            except ValueError:
                print(" Error: Please enter a valid numeric amount.")
                
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                withdraw(amount)
            except ValueError:
                print(" Error: Please enter a valid numeric amount.")
                
        elif choice == "4":
            show_history()
            
        elif choice == "5":
            print("\nThank you for using Cosmos CLI Bank. Goodbye!")
            break
            
        else:
            print("Invalid option. Please choose between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()