"""
Welcome back to the Bot project. In part 2, we'll modify the existing code by accepting user input to make it more interactive.

Let's start with the first question.

"""

# Task

"""
1.Remove the line where you declare the name variable and assign it a value.
2.Add input function to capture the user's input and add "Hello! What is your name? " 
 as the argument between the parentheses.
3.Remove the print statement to display the question only once 
 (using the input function instead of print.)
4.Replace the line where we define the age variable with the input function and use "How old are you? " 
 with the input function and save the received input in a variable called age_input.
5.Create a variable called age and use the int function to transform the input into a number like 
 age = int(age_input).
6.Remove the print function displaying "How old are you? " to not ask twice.

 """



name=input("What is your name:")
print(f"Nice to meet you {name}!")
age=input("How old are you?")
bot_age=3
age_diff=int(age)-bot_age
print(f"You are {age_diff} years older than me!,I am only {bot_age} years old!")
colour=input("What's your favorite color?")
print(f"Oh,{colour} is a beautiful color!")
