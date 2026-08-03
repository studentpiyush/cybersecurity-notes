#Goal :- Create a game where the computer randomly chooses a number, and the user keeps guessing until the correct number is found.

#Requirements :-
#Generate a random number between 1 and 100.
#Ask the user to guess the number.
#If the guess is too high, tell the user.
#If the guess is too low, tell the user.
#If the guess is correct, congratulate the user.
#Count the number of valid attempts.
#Ignore invalid guesses (outside the range 1–100).
#Keep asking until the correct number is guessed.

#English Steps (Algorithm) :-
#Start the program.
#Generate a random number between 1 and 100.
#Set the attempt counter to 1.
#Ask the user to guess a number.
#Repeat the following until the correct number is guessed:
#Check whether the number is between 1 and 100.
#If the number is invalid, ask the user to enter another number.
#If the guess is greater than the secret number, tell the user it is too high.
#If the guess is less than the secret number, tell the user it is too low.
#Increase the attempt counter for each valid incorrect guess.
#Ask the user to guess again.
#When the user guesses correctly:
#Display a congratulations message.
#Display the total number of attempts.
#End the program.

print("<========Number_Guessing_Game========>")


import random

secret_number = random.randint(1, 100)

attempt = 1

guess = int(input("Enter the number you guess : "))

while guess != secret_number:

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too Low")

    guess =int(input("Enter the number you guess : "))
    attempt += 1

print("Hooray! You guessed it right.")
print(f"You take {attempt} attempt to guess the correct number")