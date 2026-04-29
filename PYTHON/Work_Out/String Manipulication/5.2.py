"""
String Manipulation Exercise: 

Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
"""

sentence=input("Tell me a sentence:")
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","_"))
print(sentence.strip())


 