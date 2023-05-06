# opens question text file and reads the questions
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

# ask each question in order
for question in quiz_questions:
    # split the question into the question itself and its choices
    question, choices = question.split(":")
    # convert the choices string into a list
    choices = choices.strip().split(",")
    # print the question and choices
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i+1}) {choice}")
    # get the user's answer
    answer = input("Enter your answer (1-4): ")
    # get the correct answer from the dictionary
    correct_answer = quiz_answers[question.strip()]
    # check if the answer is correct
    if choices[int(answer)-1] == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")