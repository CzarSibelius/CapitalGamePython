from random import randint

def get_questions():
    with open("data.txt", "r") as data_file:
        lines = data_file.readlines()
        for line in lines:
            (question, answer) = line.split(",")
            questions[question] = answer.rstrip()
    return questions

questions = {}
questions = get_questions()

def game_loop():
    while True:
        random_question_index = randint(0, len(questions) -1)

        print("What is the capital of " + list(questions)[random_question_index] + "?")
        print("(enter 'q' to go to the main menu.)")

        answer = input()

        if answer == "q":
            break
        elif answer == list(questions.values())[random_question_index]:
            print("Correct!")
        else:
            print("Wrong answer. Correct answer was " + list(questions.values())[random_question_index])

def edit_questions():
    while True:
        print("Questions")
        print("---------")
        for index, question in enumerate(questions):
            print(str(index) + ": " + question + " " + questions[question])
        print("----------")
        print("Enter index to delete question or type a new question with 'question,answer' format to add a new question.")
        print("Enter 'q' to go back to main menu.")

        action = input()

        if action.isnumeric():
            del questions[list(questions)[int(action)]]
        elif action == "q":
            break
        else:
            (new_question, new_answer) = action.split(",")
            questions[new_question] = new_answer

        with open("data.txt", "w") as data_file:
            for question in questions:
                data_file.write(question + "," + questions[question] + "\n")
while True:
    print("Main menu")
    print("---------")
    print("1) Play the game")
    print("2) Edit questions")
    print("3) Quit")

    menuChoice = input()

    if menuChoice == "1":
        game_loop()
    elif menuChoice == "2":
        edit_questions()
    elif menuChoice == "3":
        break
