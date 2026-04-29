
# 5.Dictionary & Conditionals

"""
  Write a Python program that:
    1.Creates a dictionary representing an inventory of 3 store items with their stock counts (e.g., "apple": 10).
    2.Asks the user to enter an item name to search for.
    3.Checks if the entered item is present in the dictionary. If it is, print its stock count. If it is not, 
      print "Item out of stock". 
      
"""

items = {
    "apple" : 10,
    "banana" : 5,
    "greaps" : 8
}


item_name = input("Enter the item name:")

if item_name in items:
    print("Stock count")
else:
    print("Item out of stock")