#Goal :- Build a program that checks whether a password is strong based on a few security rules.

#Requirements

#The program should :-
#Ask the user to enter a password.
#Check if the password has at least 8 characters.
#Check if it contains at least one uppercase letter.
#Check if it contains at least one lowercase letter.
#Check if it contains at least one digit.
#Check if it contains at least one special character.
#Tell the user which requirements are satisfied.
#Tell the user which requirements are missing.

#English Steps (Algorithm) :-
#Start the program.
#Display the program title.
#Ask the user to enter a password.
#Check whether the password has at least 8 characters.
#Check whether it contains an uppercase letter.
#Check whether it contains a lowercase letter.
#Check whether it contains a digit.
#Check whether it contains a special character.
#Display the result of each check.
#If all requirements are satisfied, tell the user the password is strong.
#Otherwise, tell the user the password is weak.
#End the program.

print("<========Password_Strength_Checker========>")

password = input("Enter the Password here : ")

has_length = len(password) >= 8

if len(password) >= 8:
    print("Password has atleast or more than 8 letters")
else:
    print("Password should have atleast 8 or more letters")

has_upper = False
has_lower = False
has_digit = False

special = [ "!", "@", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "?"]

has_special = False

for character in password:
    if character .isupper():
        has_upper = True
    elif character .islower():
        has_lower = True
    elif character .isdigit():
        has_digit = True
    elif character in special:
        has_special = True

if has_upper:
    print("Password have atleast one uppercase letter")
else :
    print("should have atleast one uppercase letter")
if has_lower:
    print("password have atleast one lowercase letter")
else :
    print("should have atleast one lowercase letter")
if has_digit:
    print("password have atleast one digit")
else:
    print("should have atleast one digit")
if has_special:
    print("password have atleast one special character")
else :
    print("should have atleast one special character")

if has_length and has_upper and has_lower and has_digit and has_special:
    print("Password is strong")
else:
    print("Password is weak should follow the rules")

