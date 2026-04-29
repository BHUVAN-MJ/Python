
# 1.While Loop & Input

"""
  Write a Python program that:
    1.Uses a while loop to repeatedly prompt the user to "Type a word (or 'quit' to exit):".
    2.As long as the user's input is NOT equal to "quit", print the word in uppercase.
    Hint: You will need to ask for input once before the loop, and then again inside the loop!
    

"""

word =input("Type a word (or 'quit' to exit):")

while word != "quit":
    print(word.upper())
    word =input("Type a word(or 'quit' to exit):")
