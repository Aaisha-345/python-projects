import random
import string

def generate_password(length, include_symbols=True):
    # 03 | Project Levels: Define character sets based on requirements
    # MVP Base uses letters and digits
    chars = string.ascii_letters + string.digits
    
    # level 02 - Improve: Add punctuation and symbols
    if include_symbols:
        chars += string.punctuation
    
    # 02 | Implementation Guide: Build the password character by character
    pwd = ""
    for _ in range(length):
        pwd += random.choice(chars)
        
    return pwd

def main():
    print("--- Welcome to the Password Generator Tool ---")
    
    # 01 | MVP Requirement: Ask for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Ask user preference for symbols (Level 02 Improve)
    use_symbols = input("Include symbols/punctuation? (y/n): ").strip().lower() == 'y'

    # Level 03 - Challenge: Generate multiple options for selection
    print("\n--- Generated Password Options ---")
    for i in range(1, 4):  # Demostrating 3 options
        option = generate_password(length, include_symbols=use_symbols)
        print(f"Option {i}: {option}")

if __name__ == "_main_":
    main()