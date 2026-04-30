"""
Create a program that performs the following tasks using range():

    Print all numbers between 30 to 80 that are divisible by 4
    Print the first 8 odd numbers starting from 15
    Count backwards from 50 to 10, showing only numbers divisible by 5
    Calculate and print the product of all numbers from 1 to 30 (inclusive) that are divisible by 3
For tasks 1-3, when printing a number use the following code:

print(num, end=", ") 
The print function has an optional parameter called “end” whose default is to create a new line. 

Assigning this argument to end will override the new line after the number and instead it will add ,between numbers.

Important for Task 4: Print only the final product result as a single number (not "Product = ..." - just the number itself).

Note: The empty print() statements in the code editor are used to create blank lines between outputs, making the results easier to read.


"""
# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for i in range(30,81):
    if i % 4 == 0:
        print(i, end=", ")


print()  # Creates a new line for better readability

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
for i in range(15,30,2):
    print(i, end=", ")


print()  # Creates a new line for better readability

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for i in range(50,9,-5):
    print(i, end=", ")

print()  # Creates a new line for better readability

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
product =1

for i in range(3,31,3):
    product *= i

# Remember: print only the number, not "Product = number"

print(product)
