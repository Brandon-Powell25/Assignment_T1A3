import random 

def start_quiz():
    # opens question file and reads the questions
    with open("questions.txt", "r") as f:
        quiz_questions = f.readlines()

# open the answers file and read the answers into a dictionary
    with open("answers.txt", "r") as f:
        quiz_answers = {}
        for line in f:
            if ":" in line:
                question, answer = line.strip().split(":")
            else:
                question, answer = line.strip(), "No answer provided"
            quiz_answers[question.strip()] = answer.strip()

# ask question in order
    for i, question in enumerate(quiz_questions):
        # Questions are split into Choices and the questions themself
        question, choices = question.split(":")
        # Choice string are converted into a list
        choices = choices.strip().split(",")
        #print choices and questions
        print(f"Question {i+1}: {question}")
        for j, choice in enumerate(choice):
            print(f"{j+1} {choice}")
        # Users answers input
        answer = input("Enter your answer (1-4:)")
        #get the correct answers from dictionary
        correct_answer = quiz_answers[question.strip()]
        # If answer is incorect will check
        if choice[int(answer)-1] == correct_answer:
            print("Correct!!")
        else:
            print("Incorrect!!")