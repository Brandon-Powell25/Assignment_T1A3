import random 

class QuizFormatError(Exception):
    pass

movie_score = {}
cartoon_score = {}

def start_quiz(name, questions_file, answers_file, quiz_type):
    while True:
    
        # opens question file and reads questions
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
            
        # Shuffle Questions
        random.shuffle(quiz_questions)

        # initialize score
        score = 0

        # Display welcome message
        print(f"Welcome {name} to the Quiz! Good Luck!!!!!!\n")

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
                    print("Whoop Whoop Correct!!!\n")
                    score += 1                    
                else:
                    print(f"OH NO Incorrect!!!! Correct answer is: {correct_answer}\n")
                    break # break loop if answer is wrong
            # Except the error and will continue
            except UnboundLocalError:
                print("Error: 'choice' varibale not defined.")
                continue
            except QuizFormatError as e:
                print(e)
            except Exception as e:
                print(f"Error: {e}")

        # Based on quiz will store scores
        if quiz_type == "movie":
            movie_score[name] = score
        elif quiz_type == "cartoon":
            cartoon_score[name] = score

            # print the final score
        print(f"Your score is {score}/{len(quiz_questions)}.")  
        with open("highscores.txt", "a") as f:
            f.write(f"{name}:{score}:{quiz_type}\n")

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

def view_highscore(quiz_type):
        try:
            with open("highscores.txt", "r") as f:
                highscores = [line.strip().split(":") for line in f.readlines()]
        # except file not found and will execute the file 
        except FileNotFoundError:
            highscores = []

        
        if highscores:
            quiz_scores = {}
        for line in highscores:
            if len(line) == 3 and line[2] == quiz_type:
                name, score, qtype = line
                quiz_scores[name] = int(score)
            
        if quiz_scores:
            sorted_scores = sorted(quiz_scores.items(), key=lambda x: x[1], reverse=True)
            return sorted_scores
        return []


        


        