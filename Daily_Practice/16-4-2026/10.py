
# 10.Mixed Topics: Dictionaries, Loops & Input

"""

  Write a Python program that:
    1.Creates a dictionary menu: {"water": 2, "soda": 3}.
    2.Uses a while loop to repeatedly ask the user what they want to drink, stopping only if they type "exit".
    3.Inside the loop, check if their input exists in the menu dictionary. If yes, print the price. If no, print "Not on menu".

      
"""

menu ={
    "water" : 2,
    "soda" : 3
}

while True:
    item =input("What do you want to drink:").lower()

    if item == "exit":
        break

    if item in menu:
        print("Price:",menu[item])

    else:
        print("Not on menu")