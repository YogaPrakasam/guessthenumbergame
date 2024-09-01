# Guess the Number Game

import random

number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly in {attempts} attempts.")
        break
