from quiz_functions import start_quiz

def main_menu():
    while True:
        print("Welocme to this mutliple choice quiz game!!!")
        print("Choose an option:")
        print("1) Start Movie Quiz")
        print("2) Exit Quiz")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            play_again = start_quiz()
            if not play_again:
                print("Thank you for playing the game! Hope to see you back soon!!")
            continue
        elif choice == "2":
            print("Thank you for playing hope to see you soon!!!")
            break
        else:
            print("invalid choice, please only enter 1 or 2.")

if __name__ == "__main__":
    main_menu()