# Number guessing game

import random

secret_number = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess < secret_number:
        print("Too low")

    elif guess > secret_number:
        print("Too high")

    else:
        print("Correct!")
        print(f"You took {attempts} attempts")
        break