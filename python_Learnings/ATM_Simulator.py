#Goal :- Build a simple ATM program that allows a user to perform basic banking operations such as checking balance, depositing money, withdrawing money, and exiting the program.

# Requirements

# The program should:

# Display an ATM menu.
# Allow the user to:
# Check account balance.
# Deposit money.
# Withdraw money.
# Exit the program.
# Update the balance after every deposit or withdrawal.
# Prevent the user from withdrawing more money than the available balance.
# Reject invalid deposit or withdrawal amounts (zero or negative).
# Keep showing the menu until the user chooses to exit.

# English Steps (Algorithm)
# Start the program.
# Display the ATM title.
# Set an initial account balance.
# Repeat the following until the user chooses to exit:
# Display the ATM menu.
# Ask the user to choose an option.
# If the user chooses Check Balance, display the current balance.
# If the user chooses Deposit Money:
# Ask for the deposit amount.
# Check whether the amount is valid.
# If valid, add it to the balance.
# Display the updated balance.
# If the user chooses Withdraw Money:
# Ask for the withdrawal amount.
# Check whether the amount is valid.
# Check whether there is enough balance.
# If both conditions are satisfied, subtract the amount from the balance.
# Display the updated balance.
# Otherwise, display an appropriate error message.
# If the user chooses Exit, display a thank-you message and end the program.
# If the user enters an invalid menu option, display an error message.
# End the program.

print("<======== ATM Simulator ========>")

balance = 10000

while True:

    print("\n====== ATM MENU ======")
    print("1. Check Account Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter the option you want: ")

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        deposit = int(input("Enter the amount to deposit: "))

        if deposit <= 0:
            print("Please enter a valid amount.")
        else:
            balance += deposit
            print(f"₹{deposit} deposited successfully.")
            print(f"Current Balance: ₹{balance}")

    elif choice == "3":
        withdraw = int(input("Enter the amount to withdraw: "))

        if withdraw <= 0:
            print("Please enter a valid amount.")

        elif withdraw > balance:
            print("Insufficient balance.")

        else:
            balance -= withdraw
            print(f"₹{withdraw} withdrawn successfully.")
            print(f"Current Balance: ₹{balance}")

    elif choice == "4":
        print("Thank you for using our ATM.")
        break

    else:
        print("Invalid option. Please choose from 1 to 4.")