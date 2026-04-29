
# 7.While Loop & String Modification

"""
 Write a Python program that:
    1.Creates a variable word = "Python"..
    2.Uses a while loop that runs as long as the length of word is greater than 0.
    3.Inside the loop, print the word, then use string slicing to remove the last letter (e.g., word = word[:-1]).


"""

word = "Python"

while len(word) > 0:
    print(word)
    word =word[:-1]
  