
# 4.String Manipulation & Nested if statements
"""
  Write a Python program that acts as a simple password validator. It should::
    1.Prompt the user for a new password.
    2.Check if the password is at least 8 characters long.
    3.If it is long enough, use a nested if statement to check if the password contains a blank space " ".
    4.Reject the password if it has a space, but accept it and print a success message if it does not.
      
"""


password = input("ENter new password:")

if len(password) >= 8:
    if " " in password :
        print("password rejected:password should not contain blank space")
    else:
        print("new password created successfuly")
else:
    print("password should contain atleast contain 8 words")

