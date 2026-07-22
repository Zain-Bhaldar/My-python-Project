from random import randint 
n = randint(100, 1000)
a = int(input("Enter a number: "))

guesses = 0
while a != n:
    if a < n:
        print("Higher")
    else:
        print("Lower")
    guesses += 1
    a = int(input("Enter a number: "))

print(f"Congratulations! You guessed the number in {guesses} guesses.")