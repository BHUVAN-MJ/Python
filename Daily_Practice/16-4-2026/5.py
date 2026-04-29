
# 5.Tuple, Variables & While Loop

"""
  Write a Python program that:
    1.Creates a Tuple of numbers: (5, 10, 15).
    2.Creates variables index = 0 and total = 0.
    3.Uses a while loop to go through each number in the tuple (while index < 3).
    4.Add each number to the total variable, increase the index by 1, and print the final total outside the loop.
      
"""


number =(5,10,15)

index = 0
total = 0

while index <3:
    total += number[index]
    index +=1

print("Total",total)