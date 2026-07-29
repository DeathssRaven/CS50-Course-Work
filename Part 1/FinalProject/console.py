puzzles = [
    {
        "snippet": "def add(a, b):\n    return a - b",
        "question": "What’s wrong with this function?",
        "answer": "operator"
    },
    {
        "snippet": "for i in range(5):\nprint(i)",
        "question": "What’s wrong here?",
        "answer": "indentation"
    },
    {
        "snippet": "if True:\n    print('yes')\n  print('no')",
        "question": "What’s wrong here?",
        "answer": "indentation"
    },
    {
        "snippet": "def greet(name):\n    print('Hello ' + Name)",
        "question": "What’s wrong with this function?",
        "answer": "capital letter"
    },
    {
        "snippet": "numbers = [1, 2, 3]\nprint(numbers[3])",
        "question": "What’s wrong here?",
        "answer": "index"
    }
]

def play_game():
    score = 0
    for puzzle in puzzles:
        print("\n--- Spot The Error ---")
        print(puzzle["snippet"])
        guess = input(puzzle["question"] + "\nYour answer: ").lower().strip()

        if guess in puzzle["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", puzzle["answer"])

    print(f"\nGAME OVER! Final score: {score}/{len(puzzles)}")

play_game()
