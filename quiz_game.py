print("=== PYTHON QUIZ GAME ===")

questions = [
    ("What is the capital of France?", "paris"),
    ("What is 5 + 7?", "12"),
    ("What programming language is this game written in?", "python"),
]

score = 0

for q, ans in questions:
    user = input(q + " ").lower()
    if user == ans:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer.")

print("\nYour final score:", score, "out of", len(questions))