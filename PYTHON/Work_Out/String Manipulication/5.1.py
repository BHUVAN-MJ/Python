"""
Simple Greeting Program: Write a Python program that asks the user for their name and age,
then prints a personalized greeting message. Use both the + operator and f-strings for output.

"""

User_Name=input("What is Your Name is: ")
User_Age=input("How old are you:")
print(User_Name)
print(User_Age)
print("Hello! "+"You are "+User_Name+".You are "+User_Age+" years old")
print(f"Hello! You are {User_Name}.You are {User_Age} years old ")