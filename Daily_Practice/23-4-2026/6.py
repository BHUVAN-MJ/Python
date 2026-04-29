
# 6.For Loop & Dictionary

"""
  Write a Python program that:
    1.Creates a dictionary: {"Alice": 90, "Bob": 80}.
    2.Uses a for loop to iterate through the dictionary.
    3.Prints a formatted string using the key and value: "Alice scored 90".

      
"""

scores ={
    "alice":90,
    "bob":80
}

for name,mark in scores.items():
    print(f"{name.title()} scored {mark}")