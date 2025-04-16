#Problem Statement: Write a Python program that:
#1.Creates a list of numbers from 1 to 10.
#2.Extracts the first five elements from the list.
#3.Reverses these extracted elements.
#4.Prints both the extracted list and the reversed list
n = 10
numbers = list(range(1, n + 1))  # Create a list of numbers from 1 to 10
# Extract the first five elements
extracted_numbers = numbers[:5]  # Extract the first five elements
# Reverse the extracted elements
reversed_numbers = extracted_numbers[::-1]  # Reverse the extracted elements
# Print the extracted list and the reversed list
print("Extracted first five elements:", extracted_numbers)  # Print the extracted list
print("Reversed extracted numbers:", reversed_numbers)  # Print the reversed list