#Task 2: Write and Append Data to a File
 
#Problem Statement: Write a Python program that:
#1. Takes user input and writes it to a file named output.txt.
#2. Appends additional data to the same file.
#3. Reads and displays the final content of the file.

text = input("Enter text to write to the file: ")
# Open the file in write mode to create it and write the initial content
with open('output.txt', 'w') as file:
    file.write(text + '\n')  # Write the user input to the file
    print("Data successfully written to output.txt.")

text2 = input("Enter additional text to append: ")
# Open the file in append mode to add more content
with open('output.txt', 'a') as file:
    file.write(text2 + '\n')  # Append the additional text to the file
    print("Data successfully appended.")

print("Final content of output.txt:")
# Open the file in read mode to display its content
with open('output.txt', 'r') as file:
    content = file.read()  # Read the entire content of the file
    print(content)  # Display the content to the user
