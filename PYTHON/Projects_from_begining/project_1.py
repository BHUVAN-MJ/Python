"""
Welcome to your first Python project, during which you'll build a simple bot.

In this first part, we'll fake the conversation, but already in the second part of the project,
you'll capture input to make this a real conversation."""

# Tasks:
"""
1.Add the print function to display "Hello! What is your name?"
2.Add a variable called name and assign it a string value. Maybe your name?
3.After declaring the variable, add a second print statement. 
4.Use the f-string method to display f"Nice to meet you, {name}!".
5.Use the print function to display "How old are you?".
6.Add a variable named age and assign it a value. Feel free to use your actual age.
7.Add a variable named bot_age and assign it a value of 3.
8.Create a variable named age_difference, which subtracts the bot's age from the value of the variable age.
9.Use the print function and an f-string to display "You are {age_difference} years older than me.
   I'm only {bot_age} years old!".
10.Use the print function to display "What's your favorite color?".
11.Add a variable named color and assign it a value.
12.Use the print function and an f-string to display "Oh, {color} is a beautiful color!".

"""

print("What is your name?")
name="Bhuvan"
print(f"Nice to meet you {name}!")
print("How old are you?")
age=20
bot_age=3
age_diff=age-bot_age
print(f"You are {age_diff} years older than me!,I am only {bot_age} years old!")
print("What's your favorite color?")
colour="Black"
print(f"Oh,{colour} is a beautiful color!")
