#Problem Statement: Write a Python program that:
#1. Creates a dictionary where student names are keys and their marks are values.
#2. Asks the user to input a student's name.
#3. Retrieves and displays the corresponding marks.
#4. If the student’s name is not found, display an appropriate message.
Smarks = {'John': 85,'Alice': 92,'Bob': 78,'Diana': 88,'Ethan': 95}
# Get student name from user
student_name = input("Enter the student's name: ")
# Check if the student name exists in the dictionary
if student_name in Smarks:
    # Retrieve and display the marks
    marks = Smarks[student_name]
    print(f"{student_name}'s marks: {marks}")
else:   
    # Display an appropriate message if the student is not found
    print(f"Student '{student_name}' not found in the records.")