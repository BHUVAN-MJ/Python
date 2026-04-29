# Distributing laddus

"""
Imagine you have 5 laddus to distribute among friends.you can use a for loop to give each friend a laddu
"""

laddu = 5
friends = ["Ravi","Naveen","Uttam","Dore"]

for friend in friends:
   if laddu > 0:
        print(f"{friend} get's a laddu")
        laddu -= 1
else:
    print("No more laddu left")
