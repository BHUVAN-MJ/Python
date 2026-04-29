
#Logical Operator Practice: 
"""
a Python program that takes two numbers as input from the user and checks if:

Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not)

"""

a=int(input("Enter a Number:"))
b=int(input("Enter another Number:"))

print("a and is greater than 10:", a>10 and b>10)
print("a or b one number is less then 5:",a<5 or b<5)
print("The a is not greater than b:",not(a>b))




