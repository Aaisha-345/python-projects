 # 1. Ask for subject marks dynamically and store them in a list
marks = []
num_subjects = 3

print(f"Please enter the marks for {num_subjects} subjects:")
for i in range(num_subjects):
    m = float(input(f"Enter mark for Subject {i+1}: "))
    marks.append(m)

# 2. Calculate the average score using built-in functions
avg = sum(marks) / len(marks)

# 3. Assign a grade based on the evaluation logic
if avg >= 80:
    grade = 'A'
elif avg >= 60:
    grade = 'B'
elif avg >= 40:
    grade = 'C'
else:
    grade = 'F'

# 4. Determine Pass or Fail status
if avg >= 40:
    status = "Pass"
else:
    status = "Fail"

# 5. Display the final results
print("\n--- Final Results ---")
print(f"Average Score: {avg:.1f}")
print(f"Grade Assigned: {grade}")
print(f"Status: {status}")
# Project 07: Beginner Grade Calculator (Level 2 - Dynamic Input)

# 1. Ask for subject marks dynamically and store them in a list
marks = []
num_subjects = 3

print(f"Please enter the marks for {num_subjects} subjects:")
for i in range(num_subjects):
    m = float(input(f"Enter mark for Subject {i+1}: "))
    marks.append(m)

# 2. Calculate the average score using built-in functions
avg = sum(marks) / len(marks)

# 3. Assign a grade based on the evaluation logic
if avg >= 80:
    grade = 'A'
elif avg >= 60:
    grade = 'B'
elif avg >= 40:
    grade = 'C'
else:
    grade = 'F'

# 4. Determine Pass or Fail status
if avg >= 40:
    status = "Pass"
else:
    status = "Fail"

# 5. Display the final results
print("\n--- Final Results ---")
print(f"Average Score: {avg:.1f}")
print(f"Grade Assigned: {grade}")
print(f"Status: {status}")