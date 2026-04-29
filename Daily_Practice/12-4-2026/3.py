
# 3.While Loop & List

"""
  Write a Python program that:
    1.Creates a list: tasks = ["sweep", "mop", "dust"].
    2.Uses a while loop that runs as long as the list is not empty. (Hint: while len(tasks) > 0:)
    3.Inside the loop, use the .pop() method to remove the last item and print "Finished: " followed by the item.
  
    
"""

tasks =["sweep","mop","dust"]

while len(tasks) > 0:
    task =tasks.pop()
    print(f"Finished {task} ")