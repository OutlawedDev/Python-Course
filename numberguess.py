import random

def number_guessing_game():
    print("Welcome to number guessing game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the valid range")
                
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulation! you have guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

number_guessing_game()   
