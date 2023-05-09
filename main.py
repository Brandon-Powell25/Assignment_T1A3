from quiz_functions import start_quiz, view_highscore 

def main_menu():
    while True:
        print("Welcome to this mutliple choice quiz game!!!")
        print("Choose an option:")
        print("1) Movie Quiz")
        print("2) Cartoon Quiz")
        print("3) View HighScore")
        print("4) Exit Quiz")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            name = input("Enter your name: ")
            play_again = start_quiz(name, "questions.txt", "answers.txt", "movie")
            if not play_again:
                print("Thank you for playing the game! Hope to see you back soon!!")
            continue
        elif choice == "2":
            name = input("Enter your name!:")
            play_again = start_quiz(name, "questions2.txt", "answers2.txt", "cartoon")
            if not play_again:
                print("Thank you for playing the game! Hope to see you back soon!!")
            continue
        elif choice == "3":
            print("High Scores!")
            movie_scores = view_highscore("movie")
            cartoon_scores = view_highscore("cartoon")
            if movie_scores:
                print("Movie Quiz High Scores!!!")
                for i, (name, score) in enumerate(movie_scores):
                    print(f"{i+1}. {name} - {score}\n")
            else:
                print("No Movie highscores just yet be the first!!!!")

            if cartoon_scores:
                print("Cartoon Quiz High Scores!!!")
                for i, (name, score) in enumerate(cartoon_scores):
                    print(f"{i+1}. {name} - {score}\n")
            else:
                print("No Cartoon High Scores yet!!!!")
        elif choice == "4":
            print("Thank you for playing hope to see you soon!!!")
            break
        else:
            print("invalid choice, please only enter 1 or 2.")

if __name__ == "__main__":
    main_menu()