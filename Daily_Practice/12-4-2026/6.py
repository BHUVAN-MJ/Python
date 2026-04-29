
# 6.While Loop & Dictionary

"""
  Write a Python program that:
    1.Creates an empty dictionary called user_info.
    2.Creates a variable count = 0.
    3.Uses a while loop to run exactly 2 times.
    4.Inside the loop, ask the user for a "Key" (like name or age) and a "Value", save them into the dictionary, and add 1 to the count.
      Finally, print the dictionary.
      
"""

user_info ={}

count = 0

while count < 2:
    key =input("Enter a key:")
    value =input("Enter a value:")

    user_info[key] = [value]
    count += 1

print(user_info)