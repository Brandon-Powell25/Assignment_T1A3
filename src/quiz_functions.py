import random
from colorama import Fore, Style
import emoji

class QuizFormatError(Exception):
    pass

movie_score = {}
cartoon_score = {}

def read_files(questions_file, answers_file):
    # opens question file and reads questions
    try:
        with open(questions_file, "r") as f:
            quiz_questions = [line.strip() for line in f.readlines()]
        
        # open the answers file and read the answers into a dictionary
        with open(answers_file, "r") as f:
            quiz_answers = {}
        
            for line in f:
                if ":" in line:
                 question, answer = line.strip().split(":")
                else:
                    question, answer = line.strip(), "No answer provided"
                quiz_answers[question.strip()] = answer.strip()
        return quiz_questions, quiz_answers
    except FileNotFoundError:
        questions_file = {}

def print_question(i, question, choices):
     # print choices and questions
        print(Fore.YELLOW + f"Question {i+1}: {question}" + Style.RESET_ALL)
        for j, choice in enumerate(choices):
            print(Fore.LIGHTBLUE_EX + f"{j+1} {choice}" + Style.RESET_ALL)

def check_answer(choices, answer, correct_answer):
    # Answers is correct or incorrect it will check
    if choices[int(answer)-1] == correct_answer:
        print(Fore.YELLOW + "Whoop Whoop Correct!!! 👍\n" + Style.RESET_ALL)
        print(emoji.emojize(":grinning_face_with_big_eyes:\n"))
        return 1                   
    else:
        print(f"OH NO Incorrect!!!! Correct answer is: {correct_answer}")
        
        return 0

def store_score(name, score, quiz_type):
    # Based on quiz will store scores
    if quiz_type == "movie":
        movie_score[name] = score
    elif quiz_type == "cartoon":
        cartoon_score[name] = score

def print_and_store_final_score(name, score, total_questions, quiz_type):
    # print the final score
    print(f"Your score is {score}/{total_questions}.")  
    with open("highscores.txt", "a") as f:
        f.write(f"{name}:{score}:{quiz_type}\n")

def play_again():
    # If "y" will play again or if "n" will return to main menu      
        while True:
            # ask user if want to play again
            choice = input("Want to play again? (Y/N): ")
            if choice.lower() == "y":
            # Return true to indicate if the user wants to play again
                return True
            elif choice.lower() == "n":
            # Return true to indicate that the user want to exit
                return False
            else:
                print("Invalid Input. Please choose y or n ")

def start_quiz(name, questions_file, answers_file, quiz_type):
    while True:
        # open questions files and reads the questions
        quiz_questions, quiz_answers = read_files(questions_file, answers_file)

        # Shuffle Questions
        random.shuffle(quiz_questions)

        # initialize score
        score = 0

        # Display welcome message
        print(Fore.GREEN + f"Welcome {name} to the Quiz! Good Luck!!!!!!" + Style.RESET_ALL)

        # ask question in order
        for i, question in enumerate(quiz_questions):
            try:
                # check if there is a colon in line 
                if ":" in question:
                    # Split questions and choices
                    question, choices = question.split(":")
                    choices = choices.split(",")
                    # Shuffle answer choices
                    random.shuffle(choices)
                else:
                    # Raises an error if the format input isnt formatted right
                    raise QuizFormatError(f"Error: Question {i+1} is not formatted correctly.")

                # prints from print_question function  
                print_question(i, question, choices)

                # Users answers
                answer = input("Enter your answer (1-4): ")
                # Fetches correct answers from dictionary
                correct_answer = quiz_answers[question.strip()]
                # Call check_answer function
                score += check_answer(choices, answer, correct_answer)
                
            # Except the error and will continue
            except UnboundLocalError:
                print("Error: 'choice' varibale not defined.")
                continue
            except QuizFormatError as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")

        # Calls the store_score function
        store_score(name, score, quiz_type)
        # Calls print_and_store_final_score function 
        print_and_store_final_score(name, score, len(quiz_questions), quiz_type)
        # End of quiz fetches play_again function and if 'y' continue, 'n' will break the cycle
        if play_again():
            continue
        else:
            break

def view_highscore(quiz_type):
        # Try block
        try:
            # highscores.txt opens and reads content
            with open("highscores.txt", "r") as f:
                # Each line plit by colon and any leading whitespace is removed
                highscores = [line.strip().split(":") for line in f.readlines()]
        # except file not found and will execute the file 
        except FileNotFoundError:
            highscores = []

        quiz_scores = {}
        # see if any High score in list
        if highscores:   
            # for Loop, through every line in the highscore list         
            for line in highscores:
                # If line has 3 items and the third mataches quiz type
                if len(line) == 3 and line[2] == quiz_type:
                    # Name and Score from the line and quiz_score, extract to dictionary 
                    name, score, qtype = line
                    quiz_scores[name] = int(score)
            
        if quiz_scores:
            # Sorts quiz_score and returns it as a list of tuples
            sorted_scores = sorted(quiz_scores.items(), key=lambda x: x[1], reverse=True)
            return sorted_scores
        # Returns and empty list if no scores
        return []


        


        