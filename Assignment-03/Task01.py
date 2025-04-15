#Task 1: Calculate Factorial Using a Function 
#Problem Statement: Write a Python program that:
#1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2. Returns the calculated factorial.
#3. Calls the function with a sample number and prints the output.

def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number: "))
print(f"Factorial of {n} is: {factorial(n)}")