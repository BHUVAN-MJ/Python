
# 1.While Loop & String Manipulation

"""
  Write a Python program that:
    1.Prompts the user to enter a word.
    2.Creates an index variable starting at 0.
    3.Uses a while loop to print each letter of the word on a new line one by one using string indexing (e.g., word[index]).
    

"""


word =input("Enter a word:")

index =0

while index < len(word) :
    print(word[index])
    index +=1

