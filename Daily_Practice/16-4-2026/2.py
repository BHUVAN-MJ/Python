
# 2.Lists & While Loop

"""
  Write a Python program that:
    1.Creates two lists: inbox = ["email1", "email2", "email3"] and an empty list called archive.
    2.Uses a while loop that runs as long as inbox has items.
    3.Inside the loop, .pop() an item from inbox and .append() it to archive, then print archive.
 
      
"""

inbox =["mail1","mail2","mail3"]
archive =[]

while len(inbox) > 0:
    mail =inbox.pop()
    archive.append(mail)
    print(archive)