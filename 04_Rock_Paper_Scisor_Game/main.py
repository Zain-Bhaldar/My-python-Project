import random

def play_game():

    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        play_game()
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

def menu():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose an option:")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        play_game()
    elif choice == '2':
        print("Thank you for playing! Goodbye.")
    else:
        print("Invalid choice. Please try again.")
    menu()
menu()