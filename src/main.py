from colored import fg, bg, attr
from rich.console import Console
from rich.text import Text
from quiz_functions import start_quiz, view_highscore 

# creates a console to print formatted text to a console
console = Console()

def main_menu():
    while True:   
        # Print the text in Yellow with a party popper emoji imported from the "Rich"    
        welcome_text = Text("Welcome to this mutliple choice quiz game!!!", style='yellow')
        console.print(welcome_text, ":tada:" ) 

        # Choices to pick for Quiz in a list form with there own emoji  
        options = [
            ("1) ", "Movie Quiz 🎥"),
            ("2) ", "Cartoon Quiz 🐱"),
            ("3) ", "View High-Score 🏆"),
            ("4) ", "Exit Game ❌")
        ]
        
        options_text = Text("Choose an option:\n", style='magenta')
        # Iterates over the options list
        for number, text in options:
            # .append the numbers to red and text to blue
            options_text.append(number, style="red")
            options_text.append(text + "\n", style="blue")
        #print options_text to the console
        console.print(options_text)
        # Print Enter your choice with colored package
        choice = input(f"{bg(23)}{fg(18)}Enter your choice (1-4):{attr(0)}")
        # Option 1 Movie Quiz
        if choice == "1":
            # Name Input after you hit option 1 print in colour with colored
            name = input(f"{fg(3)}Enter your name: {attr(0)}")
            print("You will be asked 25 questions!! Best of luck!!!")
            # After name input start_quiz is called and fetches movie quiz files
            play_again = start_quiz(name, "questions.txt", "answers.txt", "movie")
            # Uses play_again function if player doesnt want to play prints messages
            if not play_again:
                print(f"{fg(4)}Thank you for playing the game! Hope to see you back soon!! {attr(0)}")
            continue
        # Option 2 Cartoon quiz
        elif choice == "2":
            # Name input for cartoon quiz
            name = input(f"{bg(102)}{fg(18)}Enter your name!: {attr(0)}")
            print("You will be asked 25 questions!! Best of luck!!!")
            # After name input start_quiz is called and fetches cartoon quiz files
            play_again = start_quiz(name, "questions2.txt", "answers2.txt", "cartoon")
            # Uses play_again function if player doesnt want to play prints messages
            if not play_again:
                print(f"{fg(4)}Thank you for playing the game! Hope to see you back soon!! {attr(0)}")
            continue
        # Option 3 View Leaderboard
        elif choice == "3":
            print(f"{bg(3)}{fg(0)} High-Scores! {attr(0)}")
            movie_scores = view_highscore("movie")
            cartoon_scores = view_highscore("cartoon")
            if movie_scores:
                print(f"{fg(23)} Movie Quiz High-Scores!!! {attr(0)}")
                for i, (name, score) in enumerate(movie_scores):
                    print(f"{i+1}. {name} - {score}\n")
            else:
                print("No Movie High-Scores just yet be the first!!!!")

            if cartoon_scores:
                print(f"{fg(15)} Cartoon Quiz High-Scores!!! {attr(0)}")
                for i, (name, score) in enumerate(cartoon_scores):
                    print(f"{i+1}. {name} - {score}\n")
            else:
                print("No Cartoon High-Scores yet!!!!")
        elif choice == "4":
            print("Thank you for playing hope to see you soon!!! 👍")
            break
        else:
            print("invalid choice, please only enter 1 or 4.")

if __name__ == "__main__":
    main_menu()