import random

def play_rock_paper_scissors():
    # 1. Store the 3 valid choices in a list
    choices = ["rock", "paper", "scissors"]
    
    # 02 Improve: Keep track of dynamic scores
    player_score = 0
    computer_score = 0
    round_number = 1
    
    print("=== Welcome to Rock, Paper, Scissors! ===")
    print("Rules: First to 2 points wins (Best of 3), or type 'quit' to exit anytime.\n")
    
    # 03 Challenge: Continuous loop (Best of 3 condition)
    while player_score < 2 and computer_score < 2:
        print(f"--- Round {round_number} ---")
        print(f"Current Score -> Player: {player_score} | Computer: {computer_score}")
        
        # 01 MVP: Get player input
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        
        # Allow the user to exit early
        if player_choice == 'quit':
            print("Thanks for playing!")
            return
            
        # Validate user input
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.\n")
            continue
            
        # 01 MVP & Instructions: Computer chooses randomly using random.choice()
        computer_choice = random.choice(choices)
        
        # 01 MVP: Show both choices
        print(f"You chose: {player_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # 01 MVP & Instructions: Determine the winner using clear if-elif-else rules
        if player_choice == computer_choice:
            print("Result: It's a draw!\n")
            
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("Result: You win this round! 🎉\n")
            player_score += 1  # Dynamic scoring
            
        else:
            print("Result: Computer wins this round! 🤖\n")
            computer_score += 1  # Dynamic scoring
            
        round_number += 1
        
    # --- Game Over Summary ---
    print("=== Final Game Over ===")
    print(f"Final Score -> Player: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won the Best of 3 match! 🏆")
    else:
        print("Computer wins the match! Better luck next time! 🦾")

# Run the project end-to-end
if __name__ == "_main_":
    play_rock_paper_scissors()