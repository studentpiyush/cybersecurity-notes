print("~~~~~~~~~~~Number_Guessing_Game~~~~~~~~~~~")

import random
random.randint(1, 100) 

secret_number = random.randint(1, 100)

guess = int(input("Guess the number: "))

if guess > secret_number:
    print("Number is too high")
elif guess < secret_number:
    print("Number is too low")
elif guess == secret_number:
    print("Hooray! You guessed it right.")
else:
    print("The number is not in between 1-100")

guess == secret_number
while cond:
    print(guess)