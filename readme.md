# Source links for coding 
Where i got some cartoon quiz and answers and source for helping in code and packages, and help with trello:

https://ahaslides.com/blog/cartoon-quiz/

https://pypi.org/project/rich/

https://pypi.org/project/colored/

https://pypi.org/project/colorama/

https://pypi.org/project/emoji/

https://www.geeksforgeeks.org/python-program-to-print-emojis/

https://www.youtube.com/watch?v=6drUzoeHZkg

https://realpython.com/python-quiz-application/

https://www.makeuseof.com/python-make-interactive-quiz-game/

https://www.bing.com/videos/search?q=how+to+make+quiz+game+in+python+with+file+handling+and+error+handling&docid=603533928359657577&mid=7C7CFB27BEB739E138E07C7CFB27BEB739E138E0&view=detail&FORM=VIRE

https://ait.instructure.com/courses/4705/pages/conference-recordings-term-1

# Source links for Github, Youtube, Trello
https://github.com/Brandon-Powell25/Assignment_T1A3

https://trello.com/b/Qb8stazi/brandon-quiz-checklist

https://youtu.be/B-qpq2NvbbQ


# Identify any code style guide or styling conventions that the application will adhere to.

- Reference the chosen style guide appropriately.

Since we are studying through Coder Academy we have been taught the PEP 8 style guide for Python. It is a widely-used set of conventions for writing Python code. Some of the key features are:
Using 4 spaces for indentation, rather than tabs.
Using snake_case for variable and function names, with all lowercase letters and underscores seperating words like_this.
using appropriate whitespace around operators and other syntax elements, such as commas and colons.
Using docstrings to document functions and modules, with a specific format for the content of each string.

Since this is what we have learnt in class, this is what I will use to format my code to make it look neat and ledgable.



# Develop a list of features that will be included in the application. It must include:

- at least THREE features
- describe each feature

### Feature 1 is a questions and answers:

1. The start_quiz function is responsiable for starting the quiz as well as asking questions checking the answers and displaying final score.

2. The while Ture loop is used to keep the game running as long as the user doing choose exit.

3. The read_files function get called to read quiz questions and answers from right file and returns them as a tuple.

3. The random.shuffle is used to shuffle all the questions and choices.

4. Score variable is used to store the users score at the end of quiz.

5. The if statement is used to check if there is a (":") in the questions if there isnt the QuizFormatError is raised to indicate that the question is formatted correctly.

6. The print_question() function is called to display the question and answer choices to the user.

7. Quiz_answers is used to fetch the correct answer for the question.

### Feature 2 is a name input/user input.

1. if the user choice option 1 or 2, they are prompted to enter their name an then the start_quiz() function is called with the appropriate quiz file and quiz type they choice either (Movie or Cartoon Quiz).

2. if the user choose option 3, the View_highscore() function get called and show both movie and cartoon highscore. Which will prompt empty if no score is yet there which is handle by in my quiz_function under View_highscore() with a try and except block which handles if a error was to be raise it will just show an empty dictionary and say no high score yet.

3. The loop will continue until the user presses 4, and prompt with a goodbye message.

### Feature 3 is a scoring system

1. Store_score() function is responsible for storing the users score basded on the quiz type, which takes three arguments -'name', 'score' and 'quiz_type'.

2. Movie_score and cartoon_score dictionaries are used to store users who toke either quiz score and store them. Scope of them is global they ca be accessed from any part of the code.

# Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

## Steps to install the application:

1. Clone my repository to you machine using https://github.com/Brandon-Powell25/Assignment_T1A3

2. Navigate to project directory using cd repo.

3. Run the "run.sh" script by using ./run.sh in your terminal. This will download all reuirements and packages as will as activate virtual enviroment and then clear the terminal and start the quiz program.

## Dependencies:

1. Python 3.10 or higher

2. Pip3 (Python package manager)

The following python packages that are required to run the quiz program will be automatically installed when you run./run.sh in your terminal these packages are:
- colorama==0.4.6
- colored==1.4.4
- emoji==2.2.0
- exceptiongroup==1.1.1
- iniconfig==2.0.0
- markdown-it-py==2.2.0
- mdurl==0.1.2
- packaging==23.1
- pluggy==1.0.0
- Pygments==2.15.1
- pytest==7.3.1
- rich==13.3.5
- tomli==2.0.1

## System/Hardware Requirements:
This multiple choice quiz game will work on any operating system that supports python3.10 or higher. Doesnt have any specific hardware requirements.

