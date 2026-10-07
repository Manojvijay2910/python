import random

def number_guessing_game():
    secret_number = random.randint(1,100)
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")

number_guessing_game()