print("<----Password_Strength_Checker---->")

password = input("Enter your Password here : ")

if len(password) >= 8:
    print("password is of eigth or more characters")
else:
    print("Password, Atleast should be of 8 or more characters")

has_upper = False

for character in password:
    if character .isupper():
        has_upper = True

if has_upper:
    print("Password has at least one uppercase letter.")
else:
    print("Password must contain at least one uppercase letter.")

has_lower = False

for character in password:
    if character .islower():
        has_lower = True

if has_lower:
    print("Password has at least one lowercse letter.")
else:
    print("Password must contain at least one lowercase letter.")

has_digit = False

for character in password:
    if character .isdigit():
        has_digit = True

if has_digit:
    print("Password has at least one digit.")
else:
    print("Password must contain at least one digit.")

special = [ "!", "@", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "?"]

has_special = False

for character in password:
    if character in special:
        has_special = True

if has_special:
    print("Password has at least one special character.")
else:
    print("Password must contain at least one special character.")