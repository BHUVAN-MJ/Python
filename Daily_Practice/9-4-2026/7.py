
# 7.Dictionary, String Manipulation & Nested if statements

"""
  Write a Python program that:
    1.Asks the user to type an email address.
    2.Checks if the character '@' is inside the string.
    3.If it is, use a nested if statement to check if the string also ends with ".com".
    4.Prints "Valid Email Structure" if both conditions pass, and specific error messages if they fail. 
      
"""
email = input("Enter your email:")

if "@" in email:
    if email.endswith(".com"):
        print("Your email structure is good")
    else:
        print("Your email structure missing '.com' ")
else:
    print("Your email missing '@' symbol")   