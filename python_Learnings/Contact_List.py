# Goal :- Build a simple Contact Book that allows a user to store and manage contacts.

# Requirements

# The program should allow the user to :-
# Add a new contact.
# View all contacts.
# Search for a contact.
# Delete a contact.
# Exit.

# Rules :-
# A contact should contain only the person's name for now.
# (We'll add phone numbers later in Version 2.)
# Don't allow duplicate names.
# If there are no contacts, tell the user:
# No contacts found.
# No contacts found.
# If the user searches for a name that doesn't exist, display an appropriate message.
# If the user tries to delete a contact that doesn't exist, display an appropriate message.
# Keep showing the menu until the user chooses Exit.

#English Steps (Algorithm) :-

# Start the program.

# Display the title.

# Create a place to store contacts.

# Repeat:

#     Show the menu.

#     Ask the user to choose an option.

#     If the user chooses Add Contact:
#         Ask for the contact name.
#         Check if it already exists.
#         If not, add it.
#         Otherwise, display a message.

#     If the user chooses View Contacts:
#         If there are contacts,
#             display all contacts.
#         Otherwise,
#             display "No contacts found."

#     If the user chooses Search Contact:
#         Ask for a contact name.
#         If found,
#             display it.
#         Otherwise,
#             display "Contact not found."

#     If the user chooses Delete Contact:
#         Ask for a contact name.
#         If found,
#             delete it.
#         Otherwise,
#             display "Contact not found."

#     If the user chooses Exit:
#         End the program.

print("<========Contact_Book========>")

Contact_names = ["Ayush", "Anand", "Vivek", "Ram", "Shyam", "Piyush", "Dev", "Tom"]

while True:
    print("Menu :- ")

    print("1. Add a new name")
    print("2. View all contacts")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Exit")

    Choose = (input("Choose from the Menu : "))

    if Choose == "1":
        New_Contact = input("Enter new Contact")
        if New_Contact in Contact_names:
            print("The name is already exists in the Contacts")
        else:
            Contact_names.append(New_Contact)
            print(f"{New_Contact}, Successfully added to the Contacts")


    elif Choose == "2":
        if len(Contact_names) == 0:
            print("No contacts found.")
        else:
            for contact in Contact_names:
                print(contact)
                    
    elif Choose == "3":
        search = input("Enter the contact you want to search")
        if search in Contact_names:
            print(search)
        else:
            print(f"no coatact exists of name {search}")

    elif Choose == "4":
        delete = input("Enter the name you want to delete")
        if delete in Contact_names:
            Contact_names.remove(delete)
        else:
            print(f"No contact found name {delete}")

    elif Choose == "5":
        print("Thank you for visiting,Come again!")
        break;

    else:
        print("Invalid option. Please choose from 1 to 5.")

print("<========Contact_Book========>")
