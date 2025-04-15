#Task 2: Using the Math Module for Calculations
#Problem Statement: Write a Python program that:
#1.Asks the user for a number as input.
#2.Uses the math module to calculate the:
#   Square root of the number
#   Natural logarithm (log base e) of the number
#   Sine of the number (in radians)
#3.Displays the calculated results.
import math

n = int(input("Enter a number: "))
sqrt_n = math.sqrt(n)
log_n = math.log(n)
sin_n = math.sin(n)

print(f"Square root: {sqrt_n}")
print(f"Logarithm: {log_n}")
print(f"Sine: {sin_n}")