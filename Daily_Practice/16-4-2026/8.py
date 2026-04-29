
# 8.String Manipulation, While Loop & Escape Sequences

"""
  Write a Python program that:
    1.Sets a string variable message = "" and a count = 1.
    2.Uses a while loop to run 3 times (while count <= 3).
    3.Inside the loop, concatenate (add) the string "Alert!\n" to message and increase count. Print message at the very end.

      
"""

message =""

count =1

while count <= 3:
    message = message + "Alert!\n"
    count += 1
    print(message)
