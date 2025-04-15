#Task 2: Sum of Integers from 1 to 50 Using a Loop
#Problem Statement: Write a Python program that:
#1. Uses a for loop to iterate over numbers from 1 to 50.
#2. Calculates the sum of all integers in this range.
#3. Displays the final sum.

sum = 0
for i in range(1, 51):
    sum += i
print("The sum of numbers from 1 to 50 is:", sum)