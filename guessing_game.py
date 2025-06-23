import random

def guessing_game():
    number = random.randint(1, 100)  # computer picks a number between 1 and 100
    guess = None
    attempts = 0

    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while guess != number:
        guess = input("Enter your guess: ")
        
        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
