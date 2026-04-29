
# 8.For Loop, List & Nested if statements

"""
  Write a Python program that:
    1.Creates a list of usernames: ["admin", "guest", "superuser"].
    2.Uses a for loop to check each username.
    3.If the username length is greater than 4, use a nested if to check if it equals "admin". If so, print "Admin found!".

      
"""

names =["admin","guest","superuser"]

for name in names:
    if len(name) > 4:
        if name =="admin":
            print("Admin found!")