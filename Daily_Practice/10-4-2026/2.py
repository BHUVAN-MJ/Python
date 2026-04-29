
# 2.Tuple, Set & Conditionals

"""
  Write a Python program that:
    1.Creates two fixed Tuples: group_a = ("apple", "banana", "orange") and group_b = ("banana", "kiwi", "grape").
    2.Converts both Tuples into Sets.
    3.Prompts the user to input a fruit name.
    4.Uses an if-else statement to check if the user's fruit exists in both sets, only one of the sets,
      or neither set. 
      
"""

fruit_name =input("Enter a fruit name:")

group_a =("apple","banana","orange")
group_b =("banana","kiwi","grape")

set_1 =set(group_a)
set_2 =set(group_b)

if fruit_name in set_1 and fruit_name in set_2:
    print("The fruit is in both sets")
elif fruit_name in set_1 or fruit_name in set_2:
    print("The fruit is in one set")
else:
    print("The fruit is not in both sets")