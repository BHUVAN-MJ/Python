
# 5.For Loop & Dictionary

"""
  Write a Python program that:
    1.Creates a dictionary of fruit prices: {"Apple": 2, "Banana": 1, "Cherry": 3}.
    2.Uses a for loop to iterate through the dictionary (this loops through the keys by default!).
    3.Prints the key and its matching value (e.g., "Apple costs 2").

      
"""

fruits ={
    "apple":2,
    "banana":1,
    "cherry":3
}

for fruit in fruits:
    print(f"{fruit} costs {fruits[fruit]}")