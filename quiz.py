quiz = {
    "What is Python? ": "language",
    "2 + 2 = ": "4",
    "Capital of India? ": "delhi"
}

score = 0

for question, answer in quiz.items():
    user_answer = input(question)

    if user_answer.lower() == answer:
        print(" Correct")
        score += 1
    else:
        print(" Wrong")

print("Your Score:", score)