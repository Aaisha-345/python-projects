# 1. Define the questions, choices, and correct answers using lists
# Each question is a dictionary containing the question text, multiple choices, and the correct option letter.
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "choices": ["A. .pt", "B. .py", "C. .python", "D. .pyt"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "choices": ["A. function", "B. fun", "C. def", "D. define"],
        "answer": "C"
    },
    {
        "question": "How do you start a comment line in Python?",
        "choices": ["A. //", "B. #", "C. /*", "D. <!--"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store ordered, mutable sequences?",
        "choices": ["A. list", "B. tuple", "C. set", "D. dictionary"],
        "answer": "A"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "choices": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    }
]

# Initialize the scoring mechanism
score = 0

print("Welcome to the Simple Quiz Game!\n" + "="*32)

# 2. Use a loop to display questions one at a time
for index, q in enumerate(questions, start=1):
    print(f"\nQuestion {index}: {q['question']}")
    
    # Display the multiple-choice options
    for choice in q['choices']:
        print(choice)
        
    # Get user input and normalize it to uppercase
    user_guess = input("Your answer (A, B, C, or D): ").strip().upper()
    
    # 3. Use an if statement to check the answer
    if user_guess == q['answer']:
        print(" Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")

# 4. Show the final score
print("\n" + "="*32)
print(f"Game Over! Your final score is: {score}/{len(questions)}")
print(f"Percentage: {(score / len(questions)) * 100}%")