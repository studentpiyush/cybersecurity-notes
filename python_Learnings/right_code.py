import random

print("~~~~~~~~~~ Number Guessing Game ~~~~~~~~~~")

secret_number = random.randint(1, 100)

attempts = 1

guess = int(input("Guess the number (1-100): "))

while guess != secret_number:

    if guess > secret_number:
        print("Number is too high")

    elif guess < secret_number:
        print("Number is too low")

    guess = int(input("Guess the number again: "))
    attempts += 1

print("🎉 Hooray! You guessed it right.")
print(f"You guessed it in {attempts} attempts.")