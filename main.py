from quiz_functions import start_quiz, view_highscore

def main_menu():
    while True:
        print("Welcome to this mutliple choice quiz game!!!")
        print("Choose an option:")
        print("1) Start Movie Quiz")
        print("2) View HighScore")
        print("3) Exit Quiz")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            name = input("Enter your name: ")
            play_again = start_quiz(name)
            if not play_again:
                print("Thank you for playing the game! Hope to see you back soon!!")
            continue
        elif choice == "2":
            highscores = view_highscore()
            if highscores:
                print("High Scores!")
                for i, (name,score) in enumerate(highscores):
                    print(f"{i+1}. {name} - {score}")
            else:
                print("No highscore just yet be the first!!!!")
        elif choice == "3":
            print("Thank you for playing hope to see you soon!!!")
            break
        else:
            print("invalid choice, please only enter 1 or 2.")

if __name__ == "__main__":
    main_menu()