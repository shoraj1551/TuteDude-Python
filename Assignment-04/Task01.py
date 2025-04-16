#Task 1: Read a File and Handle Errors 
#Problem Statement:  Write a Python program that:
#1. Opens and reads a text file named sample.txt.
#2. Prints its content line by line.
#3. Handles errors gracefully if the file does not exist.
with open('sample.txt', 'r') as file:
    try:
        # Read the file line by line
        for line in file:
            print(line.strip())  # Print each line without extra newline characters
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#Note: The file 'sample.txt' should be in the same directory as this script for it to work correctly.