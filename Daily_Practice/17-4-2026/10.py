
# 10.For Loop, String & Conditionals

"""

  Write a Python program that:
    1.Creates a variable count = 0 and asks the user to type a sentence.
    2.Uses a for loop to look at every single character in the sentence.
    3.Uses an if statement to check if the character is exactly the letter "a". If it is, add 1 to count. Print the final count at the end.

      
"""

count = 0

sentence =input("Enter a sentence:").lower()


for cha in sentence :
    if cha == "a":
        count += 1
print(count)