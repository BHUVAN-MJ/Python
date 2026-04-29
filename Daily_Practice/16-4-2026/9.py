
# 9.Lists, Conditionals & While Loop

"""
  Write a Python program that:
    1.Creates a list of numbers: [15, -3, 20, -8, 5].
    2.Uses an index variable and a while loop to check every number in the list.
    3.Uses an if statement to check if the current number is negative (< 0). If it is, replace it with 0. Print the fixed list at the end.

      
"""

numbers =[15,-3,20,-8,5]

index = 0 

while index < len(numbers) :
    if numbers[index] < 0:
      numbers[index] = 0
    index += 1

print(numbers)
   