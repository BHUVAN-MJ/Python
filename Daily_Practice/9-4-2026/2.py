
# 2.String Manipulation & Conditional Statements

"""
  Write a Python program that:
    1.Prompts the user to type in a single word.
    2.Extracts the first letter and the last letter of that word.
    3.Checks if the first and last letters are exactly the same (ignoring uppercase/lowercase differences) and
      prints an appropriate "Yes" or "No" message. 
      
"""
one_word = input("Enter one word:")

first_letter = one_word[0]
last_letter = one_word[-1]

if first_letter.lower() == last_letter.lower():
    print("Yes")
else:
    print("No")
    