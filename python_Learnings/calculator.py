#Goal :- Build a calculator that performs basic arithmetic operations based on the user's choice.

#Requirements

#The calculator should:

#Ask the user to enter the first number.
#Ask the user to enter the second number.
#Display a menu of operations.
#Allow the user to choose one operation.
#Perform the selected operation.
#Display the result.
#If the user enters an invalid option, show an error message.

#Operations:

#Addition
#Subtraction
#Multiplication
#Division
#Modulus
#Exponent (Power)

#English Steps (Algorithm) :-

#Start the program.
#Display the calculator title.
#Ask the user to enter the first number.
#Ask the user to enter the second number.
#Display the list of available operations.
#Ask the user to choose an operation.
#Check which operation the user selected.
#Perform the corresponding calculation.
#Display the result.
#If the user enters an invalid option, display an error message.
#End the program.

print("<========Simple_Calculator========>")

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("Available Operation :- ")

print("1. + ")
print("2. - ")
print("3. * ")
print("4. / ")
print("5. % ")
print("6. ** ")

Choice = input("Choose an Operation from the list given above : ")

if Choice == "1":
    print("Addition of a and b is : ",a + b)
elif Choice == "2":
    print("Subtraction of a and b is : ",a - b)
elif Choice == "3":
    print("Multiplication of a and b is : ",a * b)
elif Choice == "4":
    print("Division of a and b is : ",a / b)
elif Choice == "5":
    print("Remainder of a / b is : ",a % b)
elif Choice == "6":
    print("Power & Exponent is : ",a ** b)
else:
    print("Please enter a valid option from the list.")