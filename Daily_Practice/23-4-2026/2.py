
# 2.For Loop & List Manipulation

"""
  Write a Python program that:
    1.Creates an empty list called evens.
    2.Uses a for loop with range(2, 11, 2) (which generates 2, 4, 6, 8, 10).
    3.Appends each number to the evens list and prints the list.
 
      
"""

evens =[]

for i in range(2,11,2):
    evens.append(i)
    print(evens)