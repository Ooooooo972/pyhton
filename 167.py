# Simple quiz program with 2 questions

# Question 1
print("Question 1: What is the capital of France?")
print("a) Berlin")
print("b) Madrid")
print("c) Paris")
print("d) Rome")
answer1 = input("Your answer (a/b/c/d): ")

# Question 2
print("\nQuestion 2: Which planet is known as the Red Planet?")
print("a) Earth")
print("b) Venus")
print("c) Mars")
print("d) Jupiter")
answer2 = input("Your answer (a/b/c/d): ")

# Checking answers
score = 0
if answer1.lower() == 'c':
    score += 1
if answer2.lower() == 'c':
    score += 1

# Result
print(f"\nYou got {score} out of 2 correct!")
