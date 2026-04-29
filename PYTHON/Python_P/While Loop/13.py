# While loop

# Nested while 

"""
let's simulate a snack machine that allows users to buy snacks as long as both the machine has snacks
and the users has money.

"""

snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"snacks available: {snacks_available}.money:${money}")
    buy = input("Do you want to buy a sanck for $ 5?.(yes/no):").lower()

    if buy == "yes" and money >=5:
        snacks_available -= 1
        money -= 5
        print("Sanck purchased!")
    else:
        print("No purchase made.")

print("Either snacks are sold out or you are out of money.")