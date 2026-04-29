
# 2.Lists & Advanced Dictionaries

"""
  Write a Python program that:
    1.Creates a dictionary representing a user's permissions, where the key is the username (e.g., "john_doe") and the value is a List of 
      permissions: ["read", "write"].
    2.Prompts the user to enter a username to check, and then prompts them for an action they want to do (like "delete" or "read").
    3.Checks if the username exists in the dictionary. If yes, check if the action is inside that user's List of permissions,
      and print either "Access Granted" or "Access Denied"
 
      
"""

permission ={
    "ravi":["read","write"],
    "naveen":["read"],
    "uttam":["read","write","delete"],
    "akhil":["delete"]
}

username =input("Enter user name:").lower()
action =input("Enter th action:").lower()


if username in permission:
    if action in permission[username]:
      print("Access Granted")
    else:
       print("Access Denied")
else:
   print("Didn't find the user name,try again")