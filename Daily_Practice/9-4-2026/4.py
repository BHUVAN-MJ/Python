
# 4.Set & String Manipulation

"""
  Write a Python program that:
    1.Takes a single string of space-separated tags from the user (e.g., "python code bug error").
    2.Splits that string into a list and then converts it into a Set.
    3.Adds a predefined tag "debug" to the set.
    4.Prints the total number of unique tags currently in the Set.
      
"""

tags = input("Enter tags separated by space:")

tag_set =set(tags.split())
tag_set.add("debug")

print("Total unique tags:",len(tag_set))








