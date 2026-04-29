
# 5.While Loop & List Popping

"""
  Write a Python program that:
    1.Creates a list of tasks: ["Eat", "Code", "Sleep"].
    2.Uses a while loop that runs as long as the length of the list is greater than 0.
    3.Inside the loop, use .pop() to remove and print the last item.

      
"""

task =["eat","code","sleep"]

while len(task) > 0:
    temp =task.pop()
    print(temp)