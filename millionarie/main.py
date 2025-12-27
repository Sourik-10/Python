# List of questions
questions = [
    [
        "Who is the founder of Microsoft?",
        "Bill Gates",
        "Steve Jobs",
        "Mark Zuckerberg",
        "Larry Page",
        "A"
    ],
    [
        "Which programming language is known as the mother of all languages?",
        "Python",
        "C",
        "Java",
        "Assembly",
        "B"
    ],
    [
        "Who invented the World Wide Web (WWW)?",
        "Bill Gates",
        "Tim Berners-Lee",
        "Elon Musk",
        "Mark Zuckerberg",
        "B"
    ],
    [
        "What is the capital of India?",
        "Mumbai",
        "Kolkata",
        "New Delhi",
        "Chennai",
        "C"
    ],
    [
        "Which company owns Android?",
        "Apple",
        "Microsoft",
        "Samsung",
        "Google",
        "D"
    ],
    [
        "Which planet is known as the Red Planet?",
        "Earth",
        "Mars",
        "Jupiter",
        "Venus",
        "B"
    ],
    [
        "Who is known as the Father of Computers?",
        "Alan Turing",
        "Charles Babbage",
        "Dennis Ritchie",
        "Tim Berners-Lee",
        "B"
    ],
    [
        "What does CPU stand for?",
        "Central Program Unit",
        "Central Processing Unit",
        "Computer Processing Unit",
        "Control Processing Unit",
        "B"
    ],
    [
        "Which data structure uses FIFO principle?",
        "Stack",
        "Tree",
        "Queue",
        "Graph",
        "C"
    ],
    [
        "Which language is primarily used for web page structure?",
        "CSS",
        "JavaScript",
        "Python",
        "HTML",
        "D"
    ]
]

# Prize money for each correct answer
prizes = [
    "₹ 1,000",
    "₹ 2,000",
    "₹ 3,000",
    "₹ 5,000",
    "₹ 10,000",
    "₹ 20,000",
    "₹ 40,000",
    "₹ 80,000",
    "₹ 1,60,000",
    "₹ 3,20,000"
]

print("🎉 Welcome to the Millionaire Quiz Game 🎉")

i = 0  # Prize index

# Loop through each question
for question in questions:
    print("\n" + question[0])
    print("A. " + question[1])
    print("B. " + question[2])
    print("C. " + question[3])
    print("D. " + question[4])

    # Take user input
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Check the answer
    if answer == question[5]:
        print("✅ Correct!")
        print(f"You won {prizes[i]}")
        i += 1
    else:
        print("❌ Wrong!")
        print(f"The correct answer is {question[5]}.")
        print(f"You take home {prizes[i-1] if i > 0 else '₹ 0'}")
        break

# If all questions are answered correctly
if i == len(questions):
    print("\n🎊 Congratulations! You won the maximum prize! 🎊")
