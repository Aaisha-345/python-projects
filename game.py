import random

def play_guessing_game():
    print("\n--- Welcome to the Number Guessing Game! ---")
    
    # 1. Pick a random number from 1 to 20 (MVP)
    secret_number = random.randint(1, 20)
    attempts = 0  # Track number of attempts (Improvement)
    
    # 2. While loop for guesses (MVP)
    while True:
        user_input = input("Guess a number between 1 and 20: ").strip()
        
        # Check for bad input: non-integer validation (Improvement)
        if not user_input.isdigit():
            print("Invalid input! Please enter a valid whole number.")
            continue
            
        guess = int(user_input)
        
        # Check for bad input: out of bounds validation (Improvement)
        if guess < 1 or guess > 20:
            print(" Out of bounds! Your guess must be between 1 and 20.")
            continue
            
        attempts += 1  # Increment valid attempts
        
        # 3. Check the guess against the secret number (MVP)
        if guess < secret_number:
            print(" Too low! Try again.")
        elif guess > secret_number:
            print(" Too high! Try again.")
        else:
            print(f" Correct! You found the secret number {secret_number} in {attempts} attempts!")
            return attempts  # Return the score to track the high score

def main():
    high_score = None  # Track high score (Challenge)
    
    while True:
        # Run one complete game session
        score = play_guessing_game()
        
        # Update high score (Challenge)
        if high_score is None or score < high_score:
            high_score = score
            print(f" New High Score! Fewest attempts: {high_score}")
        else:
            print(f" Current High Score to beat: {high_score} attempts")
            
        # Allow replay option (Challenge)
        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay not in ['y', 'yes']:
            print("\n Thanks for playing! Final High Score:", high_score)
            break

if __name__ == "__main__":
    main()