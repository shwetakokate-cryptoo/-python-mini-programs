# Simple Quiz Game in Python

# This program asks multiple-choice questions
# and calculates the final score.

# Quiz Questions

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },

    {
        "question": "Which language is mainly used for Python development?",
        "options": ["A. Java", "B. C++", "C. Python", "D. Swift"],
        "answer": "C"
    },

    {
        "question": "Which data type stores True or False values?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. func", "D. def"],
        "answer": "D"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Central Program Utility"
        ],
        "answer": "B"
    }
]

# Function to Run Quiz

def run_quiz():

    score = 0

    print("===================================")
    print("         SIMPLE QUIZ GAME")
    print("===================================")

    # Loop through all questions
    for index, q in enumerate(questions, start=1):

        print(f"\nQuestion {index}:")
        print(q["question"])

        # Display options
        for option in q["options"]:
            print(option)

        # Take user answer
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        # Check answer
        if user_answer == q["answer"]:
            print("Correct Answer! ✅")
            score += 1
        else:
            print("Wrong Answer! ❌")
            print(f"Correct Answer: {q['answer']}")


    # Display Final Score

    print("\n===================================")
    print("             QUIZ RESULT")
    print("===================================")

    print(f"Your Final Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100

    print(f"Percentage: {percentage:.2f}%")

    # Performance Message
    if percentage >= 80:
        print("Excellent Performance! 🌟")

    elif percentage >= 50:
        print("Good Job! 👍")

    else:
        print("Keep Practicing! 📚")

# Main Program


while True:

    run_quiz()

    # Ask user to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing the quiz!")
        break
