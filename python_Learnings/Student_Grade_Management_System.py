# Goal :Build a program that helps a teacher manage student records and marks.

# Requirements :-

# The program should allow the user to:

# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Update Student Marks
# 5. Delete Student
# 6. Exit

# Rules :- 
# Each student has:
# Name
# Marks
# Don't allow duplicate student names.
# Marks must be between 0 and 100.
# If the user enters marks outside this range, display an error.
# If there are no students, display:
# No student records found.
# If a searched student doesn't exist, display an appropriate message.
# If the user tries to update or delete a student who doesn't exist, display an appropriate message.
# Keep showing the menu until the user chooses Exit.

# English Steps (Algorithm) :- 
# Start the program.
# Display the program title.
# Create a list to store student names.
# Create another list to store student marks.
# Repeat the following until the user chooses to exit:
# Display the menu.
# Ask the user to choose an option.
# If the user chooses Add Student:
# Ask for the student's name.
# Check whether the name already exists.
# If it already exists, display an appropriate message.
# Otherwise:
# Ask for the student's marks.
# Check whether the marks are between 0 and 100.
# If the marks are valid, add the student's name to the student names list.
# Add the student's marks to the student marks list.
# Display a success message.
# Otherwise, display an error message.
# If the user chooses View All Students:
# Check whether there are any student records.
# If there are no records, display :- No student records found.
# Otherwise, display every student's name and marks.
# If the user chooses Search Student:
# Ask for the student's name.
# Check whether the student exists.
# If the student exists, display the student's name and marks.
# Otherwise, display an appropriate message.
# If the user chooses Update Student Marks:
# Ask for the student's name.
# Check whether the student exists.
# If the student exists:
# Ask for the new marks.
# Check whether the marks are between 0 and 100.
# If valid, update the student's marks.
# Otherwise, display an error message.
# If the student does not exist, display an appropriate message.
# If the user chooses Delete Student:
# Ask for the student's name.
# Check whether the student exists.
# If the student exists:
# Delete the student's name.
# Delete the student's marks.
# Display a success message.
# Otherwise, display an appropriate message.
# If the user chooses Exit:
# Display a thank-you message.
# End the program.
# If the user enters an invalid menu option:
# Display an error message.
# End the program.

print("<======== Student Grade Management System ========>")

student_names = ["Ayush", "Anand", "Vivek"]
student_marks = [85, 92, 76]

while True:

    print("\n====== MENU ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        new_name = input("Enter student name: ")

        if new_name in student_names:
            print("Student already exists.")

        else:
            marks = int(input("Enter student marks (0-100): "))

            if marks >= 0 and marks <= 100:
                student_names.append(new_name)
                student_marks.append(marks)
                print("Student added successfully.")

            else:
                print("Marks must be between 0 and 100.")

    elif choice == "2":

        if len(student_names) == 0:
            print("No student records found.")

        else:
            print("\nStudent Records")
            for i in range(len(student_names)):
                print(student_names[i], "-", student_marks[i])

    elif choice == "3":

        name_to_search = input("Enter student name: ")

        if name_to_search in student_names:

            index = student_names.index(name_to_search)

            print("Student Name :", student_names[index])
            print("Student Marks:", student_marks[index])

        else:
            print("Student not found.")

    elif choice == "4":

        name_to_update = input("Enter student name: ")

        if name_to_update in student_names:

            index = student_names.index(name_to_update)

            new_marks = int(input("Enter new marks: "))

            if new_marks >= 0 and new_marks <= 100:
                student_marks[index] = new_marks
                print("Marks updated successfully.")

            else:
                print("Marks must be between 0 and 100.")

        else:
            print("Student not found.")

    elif choice == "5":

        name_to_delete = input("Enter student name: ")

        if name_to_delete in student_names:

            index = student_names.index(name_to_delete)

            student_names.remove(name_to_delete)
            student_marks.pop(index)

            print("Student deleted successfully.")

        else:
            print("Student not found.")

    elif choice == "6":

        print("Thank you for using the Student Grade Management System.")
        break

    else:
        print("Invalid option. Please choose between 1 and 6.")