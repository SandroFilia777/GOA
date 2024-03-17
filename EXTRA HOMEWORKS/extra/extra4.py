# not mine datosi

import random

def generate_random_number():
    """
    Generate a random number between 1 and 100.
    """
    return random.randint(1, 100)

def main():
    """
    The main function implementing the number guessing game logic.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = generate_random_number()
    num_attempts = 10

    for attempt in range(num_attempts):
        guess = int(input(f"Attempt {attempt + 1}/{num_attempts}: Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number ({number_to_guess}) in {attempt + 1} attempts.")
            break
    else:
        print(f"Sorry, you didn't guess the number. The number was {number_to_guess}.")


if __name__ == "__main__":
    main()