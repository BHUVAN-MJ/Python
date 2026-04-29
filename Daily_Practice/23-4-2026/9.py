
# 9.Nested Logic: For Loop & If Statements

"""
  Write a Python program that:
    1.Creates a list of words: ["cat", "elephant", "dog", "hippopotamus"].
    2.Uses a for loop to check each word.
    3.Uses an if statement to print the word ONLY if its length is greater than 5 letters.

      
"""

words =["cat","elephat","dog","hippopotamus"]

for word in words :
    if len(word) > 5:
        print(word)