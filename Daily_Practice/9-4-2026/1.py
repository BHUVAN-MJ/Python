
# 1.Input, Variables & Escape Sequences

"""
  Write a Python program that:
    1.Asks the user for their name, their favorite food, and their age.
    2.Stores all three inputs in separate variables of appropriate data types.
    3.Prints a single greeting containing all the details, using an escape sequence (\n or \t) 
      to place the favorite food on a separate, indented line.

"""

user_name = input("Enter your name:")
favorite_food = input("Enter your favorite food:")
user_age = int(input("Enter your age:"))

print(f"Your name is {user_name}.Your {user_age} years old.\n Your favorite food is {favorite_food}")