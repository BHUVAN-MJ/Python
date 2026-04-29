
# 9.While Loop & Nested if statements

"""
  Write a Python program that:
    1.Sets a variable guess = "".
    2.Uses a while loop that runs while guess != "admin".
    3.Inside the loop, prompt the user for a password. If the guess is "password", use a nested if to print "Too obvious, try again!".

      
"""

guess =""

while guess != "admin":
    guess =input("Enter a password:")

    if guess == "password":
        print("Too obvious,try again!")