questions = [
    {
        "question": "What is the output of: print(type([]))?",
        "options": ["a. <class 'list'>", "b. <class 'dict'>", "c. <class 'tuple'>", "d. <class 'set'>"],
        "answer": "a"
    },
    {   "3.question": "What is the correct file extension for Python files?",
        "options": ["a. .pt", "b. .py", "c. .pyt", "d. .p"],
        "answer": "b"
    },
    {  
        "4.question": "Which of the following is a Python tuple?",
        "options": ["a. [1, 2, 3]", "b. {1, 2, 3}", "c. (1, 2, 3)", "d. {'a': 1}"],
        "answer": "c"
    },
    {
        "5.question": "What is the output of 3 * '7'?",
        "options": ["a. 21", "b. 777", "c. 10", "d. Error"],
        "answer": "b"
    },
    {
        "6.question": "Which keyword is used to define a function in Python?",
        "options": ["a. define", "b. def", "c. function", "d. lambda"],
        "answer": "b"
    },
    {
        "7.question": "Which of the following is not a valid data type in Python?",
        "options": ["a. int", "b. float", "c. real", "d. str"],
        "answer": "c"
    },
    {
        "8.question": "What does the len() function do?",
        "options": ["a. Calculates length", "b. Calculates sum", "c. Finds max", "d. Converts to list"],
        "answer": "a"
    },
    {
        "9.question": "Which of the following is a mutable data type?",
        "options": ["a. tuple", "b. list", "c. str", "d. int"],
        "answer": "b"
    },
    {
        "10.question": "Which keyword is used for loops in Python?",
        "options": ["a. loop", "b. iterate", "c. for", "d. repeat"],
        "answer": "c"
    },
    {
        "11.question": "Which operator is used for exponentiation?",
        "options": ["a. ^", "b. **", "c. //", "d. %"],
        "answer": "b"
    },
    {
        "12.question": "What is the output of: bool('False')?",
        "options": ["a. True", "b. False", "c. Error", "d. None"],
        "answer": "a"
    },
    {
        "13.question": "Which of the following is used to define a dictionary?",
        "options": ["a. {}", "b. []", "c. ()", "d. ||"],
        "answer": "a"
    },
    {
        "14.question": "Which of the following functions returns the largest item?",
        "options": ["a. max()", "b. largest()", "c. top()", "d. upper()"],
        "answer": "a"
    },
    {
        "15.question": "Which function is used to accept input from the user?",
        "options": ["a. scanf()", "b. input()", "c. gets()", "d. read()"],
        "answer": "b"
    },
    {
        "16.question": "What is the result of: 10 // 3?",
        "options": ["a. 3.33", "b. 3", "c. 4", "d. Error"],
        "answer": "b"
    },
    {
        "17.question": "What is used to handle exceptions in Python?",
        "options": ["a. try/except", "b. do/catch", "c. handle/error", "d. try/catch"],
        "answer": "a"
    },
    {
        "18.question": "Which module in Python is used for random number generation?",
        "options": ["a. math", "b. random", "c. sys", "d. os"],
        "answer": "b"
    },
    {
        "19.question": "Which method converts a string to lowercase?",
        "options": ["a. lower()", "b. toLower()", "c. lowercase()", "d. down()"],
        "answer": "a"
    },
    {
        "20.question": "Which of the following is used to exit a loop?",
        "options": ["a. exit", "b. break", "c. continue", "d. quit"],
        "answer": "b"
    }
]



def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ").lower()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is '{q['answer']}'")

    print(f"\nQuiz completed. Your score is {score}/{len(questions)}")


def main():
    print("Welcome to the Python Interview Quiz Game!")
    print("------------------------------------------")
    start = input("Do you want to start the quiz? (yes/no): ").lower()
    if start == "yes":
        run_quiz(questions)
    else:
        print("Quiz exited. Goodbye!")


