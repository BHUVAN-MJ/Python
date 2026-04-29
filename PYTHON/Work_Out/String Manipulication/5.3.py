"""
Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.

"""

text=input("Enter a string:")
no_space=text.replace(" ","")
print(len(no_space))
