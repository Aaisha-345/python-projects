class CalculationHistory:
    def __init__(self):
        self.history_list = []

calculation_history = CalculationHistory()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Error handling for division by zero (Improvement requirement)
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def power(a, b):
    return a ** b

def percentage(a, b):
    # Calculates a% of b
    return (a / 100) * b

def show_history():
    if not calculation_history:
        print("\n--- No history recorded yet. ---")
    else:
        print("\n--- Calculation History ---")
        for index, record in enumerate(calculation_history, 1):
            print(f"{index}. {record}")

def main():
    print("====================================")
    print("    Welcome to Simple Calculator    ")
    print("====================================")
    
    while True:
        print("\nAvailable Operations:")
        print(" +  : Addition")
        print(" -  : Subtraction")
        print(" *  : Multiplication")
        print(" /  : Division")
        print(" ^  : Power (a raised to b)")
        print(" %  : Percentage (a% of b)")
        print(" h  : View Calculation History")
        print(" q  : Quit/Exit Safely")
        
        # Safe exit check
        operator = input("\nChoose an operator or action: ").strip()
        
        if operator.lower() == 'q':
            print("Thank you for using Simple Calculator. Goodbye!")
            break
            
        if operator.lower() == 'h':
            show_history()
            continue

        if operator not in ['+', '-', '*', '/', '^', '%']:
            print("Invalid operator! Please select a valid option.")
            continue

        # Input gathering with basic float parsing
        try:
            num1 = float(input("Enter the first number (a): "))
            num2 = float(input("Enter the second number (b): "))
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")
            continue

        # Operation processing logic
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '^':
            result = power(num1, num2)
        elif operator == '%':
            result = percentage(num1, num2)

        # Display result and log to history
        print(f"\nResult: {result}")
        if not str(result).startswith("Error"):
            calculation_history.append(f"{num1} {operator} {num2} = {result}")

if __name__ == "_main_":
    main()