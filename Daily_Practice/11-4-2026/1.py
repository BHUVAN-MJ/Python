
# 1.String Manipulation & String Slicing

"""
  Write a Python program that:
    1.Asks the user to enter their 16-digit credit card number as a single string.
    2.Checks if the length of the string is exactly 16 characters.
    3.If it is, use string slicing to hide the first 12 digits, combine it with "****-****-****-", and print the safe version. 
     If it is not, print an error message.
    

"""

card_number =input("Enter your 16-digit credit card number:")

if len(card_number) == 16:
    last_four =card_number[-4:]
    masked = "****-****-****-****-" + last_four
    print(masked)
else:
    print("Error:Card number must be exactly 16 degit")