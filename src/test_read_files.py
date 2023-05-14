from quiz_functions import read_files

# Testing the read file to see if they match
def test_read_files__with_25_questions():
    # Fetches correct name of file contain the questions for first test
    questions_file = "questions.txt"
    # Fetches correct name of file contain the answers for first test
    answers_file = "answers.txt"
    # specified filed are calling the function read_files to read questions and answers
    actual_questions, actual_answers = read_files(questions_file, answers_file)
    # Asserting if that the 25 is equal to the amount of questions and answers
    assert len(actual_questions) == 25
    assert len(actual_answers) == 25


def test_read_files_with_18_questions():
    # Fetches correct name of file contain the questions for second test
    questions_file = "questions2.txt"
    # Fetches correct name of file contain the answers for second test
    answers_file = "answers2.txt"
    # specified filed are calling the function read_files to read questions and answers
    actual_questions, actual_answers = read_files(questions_file, answers_file)
    # Asserting if that the 25 is equal to the amount of questions and answers
    assert len(actual_questions) == 18
    assert len(actual_answers) == 18 

# Failed test

# test_quiz_functions.py .F                                                                                                                                                                                [100%]

# FAILURES 
# def test_read_files_with_18_questions

#    def test_read_files_with_18_questions():
#        questions_file = "question2.txt"
#        answers_file = "answers2.txt"
    
# >       actual_questions, actual_answers = read_files(questions_file, answers_file)

#test_quiz_functions.py:18: 
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# questions_file = 'question2.txt', answers_file = 'answers2.txt'

#    def read_files(questions_file, answers_file):
#        # opens question file and reads questions
#>           with open(questions_file, "r") as f:
#E           FileNotFoundError: [Errno 2] No such file or directory: 'question2.txt'

#quiz_functions.py:11: FileNotFoundError
# short test summary info 
#FAILED test_quiz_functions.py::test_read_files_with_18_questions - FileNotFoundError: [Errno 2] No such file or directory: 'question2.txt'

# Passed test for my Read_files feature

# ============================================================================================= test session starts ==============================================================================================
# platform linux -- Python 3.10.6, pytest-7.3.1, pluggy-1.0.0
# rootdir: /mnt/c/Users/ninja/Desktop/BrandonPowell_T1A3
# collected 2 items

#test_quiz_functions.py ..                                                                                                                                                                                [100%]

# ============================================================================================== 2 passed in 0.29s