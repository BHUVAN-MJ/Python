
# 6.Build a frequency counter

"""
  Write a Python program that:
    1.Ask the user to enter a word.
    2.Use a loop to count how many times each letter appears.
    3.Store the counts in a dictionary and print it.

      
"""

word =input("Enter a word:").lower()

count ={}

for letter in word:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] =1
print(count)
      
