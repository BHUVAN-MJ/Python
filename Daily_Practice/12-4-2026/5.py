
# 5.While Loop & Set Manipulation

"""
  Write a Python program that:
    1.Creates a Set containing the numbers {10, 20, 30}.
    2.Uses a while loop that runs as long as the length of the set is greater than 0.
    3.Inside the loop, remove an item using .pop() and print it. 

      
"""

numbers ={10,20,30}

while len(numbers) > 0:
    num =numbers.pop()
    print(num)
    