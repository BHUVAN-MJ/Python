
# 1.While Loop & Input Validation

"""
  Write a Python program that:
    1.Uses a while loop to ask the user to "Type 'yes' to agree:".
    2.Keeps asking them until they finally type "yes".
    3.Prints "Thank you!" when the loop ends.

"""

while True :
    word =input("Enter 'Yes' to agree:").lower()
    if word == "yes":
      break
print("Thank You")
