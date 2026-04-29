
# 10.The Menu Totalizer (Dictionary, List, Operators)

"""

  Write a Python program that:
    1.Creates a Dictionary of prices: {"Burger": 10, "Fries": 5, "Soda": 3}.
    2.Prompts the user to enter two items from the menu, one by one.
    3.Uses a conditional to check if both items exist in the dictionary.
    4.If both exist, retrieve their values, add them together using math operators, add a standard $2 delivery fee to the total, 
      and print the final bill.
       
"""

menu ={
    "Burger":10,
    "Fries":5,
    "Soda":3
}

item1 =input("Enter the item you want:")
item2 =input("Enter the item you want:")

if item1 in menu and item2 in menu:
     total =menu[item1] + menu[item2] + 2
     print("Your total with delivery fee is:",total)
else:
     print("The item that you ordered is finished!")


