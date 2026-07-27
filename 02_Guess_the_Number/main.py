from random import randint
def restart_game():
    choice = input("Do you want to play again? (y/n): ")
    if choice.lower() == "y":
        main_menu()
    elif choice.lower() == "n":
        print("Thank you for playing! Goodbye.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        restart_game()

def main_menu():
    print("Welcome to Guess the Number!")
    print("Choose a difficulty level:")
    print("1. Easy (1-100)")
    print("2. Medium (1-1000)")
    print("3. Hard (1-10000)")
    choice = input("Enter your choice (1-3): ")
    guesses = 1
    while choice not in ["1", "2", "3"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1-3): ")
    while True:
        if choice == "1":
            number = randint(1, 100)
            max_attempts = 10
            print(f"You have {max_attempts} attempts to guess the number.")
            try:
                player_number = int(input("Enter a number between 1 and 100: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return main_menu()
            while player_number != number:
                if player_number < 1 or player_number > 100:
                    print("Invalid input. Please enter a number between 1 and 100.")
                    return main_menu()
                elif player_number < number:
                    print("Higher")
                else:
                    print("Lower")
                guesses += 1
                if guesses >= max_attempts:
                    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
                    return restart_game()
                try:
                    player_number = int(input("Enter a number between 1 and 100: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    return main_menu()
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            return restart_game()

        elif choice == "2":
            number = randint(1, 1000)
            max_attempts = 15
            print(f"You have {max_attempts} attempts to guess the number.")
            try:
                player_number = int(input("Enter a number between 1 and 1000: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return main_menu()
            while player_number != number:
                if player_number < 1 or player_number > 1000:
                    print("Invalid input. Please enter a number between 1 and 1000.")
                    return main_menu()
                elif player_number < number:
                    print("Higher")
                else:
                    print("Lower")
                guesses += 1
                if guesses >= max_attempts:
                    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
                    return restart_game()
                try:
                    player_number = int(input("Enter a number between 1 and 1000: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    return main_menu()
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            return restart_game()
        
        elif choice == "3":
            number = randint(1, 10000)
            max_attempts = 25
            print(f"You have {max_attempts} attempts to guess the number.")
            try:
                player_number = int(input("Enter a number between 1 and 10000: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                return main_menu()
            while player_number != number:
                if player_number < 1 or player_number > 10000:
                    print("Invalid input. Please enter a number between 1 and 10000.")
                    return main_menu()
                elif player_number < number:
                    print("Higher")
                else:
                    print("Lower")
                guesses += 1
                if guesses >= max_attempts:
                    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
                    return restart_game()
                try:
                    player_number = int(input("Enter a number between 1 and 10000: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    return main_menu()
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            return restart_game()
        
        else:
            print("Invalid choice. Please try again.")
            return main_menu()

main_menu()