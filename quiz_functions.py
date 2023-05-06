import random 

def start_quiz():
    # opens question file and reads questions
    with open("questions.txt", "r") as f:
        quiz_questions = [line.strip() for line in f.readlines()]

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
        try:
            # Split questions and choices
            question, choices = question.split(":")
            choices = choices.split(",")

            # print choices and questions
            print(f"Question {i+1}: {question}")
            for j, choice in enumerate(choices):
                print(f"{j+1} {choice}")
            # Users answers
            answer = input("Enter your answer (1-4): ")
            # Fetches correct answers from dictionary
            correct_answer = quiz_answers[question.strip()]
            # Answers is incorrect it will check
            if choices[int(answer)-1] == correct_answer:
                print("Whoop Whoop Correct!!!")
            else:
                print(f"OH NO Incorrect!!!! Correct answer is: {correct_answer}")
        except UnboundLocalError:
            print("Error: 'choice' varibale not defined.")
            continue
        except Exception as e:
            print(f"Error: {e}")
            break

    while True:
        choice = input("Want to play again? (Y/N): ")
        if choice.lower() == "y":
            # Return true to indicate if the user wants to play again
            return True
        elif choice.lower() == "n":
            # Return true to indicate that the user want to exit
            return False
        else:
            print("Invalid Input. Please choose 1 or 2 ")


        