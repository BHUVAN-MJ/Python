
#Basic Dictionary Operations:

"""
Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary.

"""

famous_dishes={
    "hassan":"akki rotti",
    "bengaluru":"bisi bele bath",
    "shivamogga":"kadubu",
    "huballi":"girmit",
    "davanagere":"dosa"
}

new_city={"mangaluru":"neer dosa"}
famous_dishes.update(new_city)
print(famous_dishes)


famous_dishes["bengaluru"]="ragi mudde"

famous_dishes.pop("davanagere")
print(famous_dishes)

del famous_dishes["shivamogga"]
print(famous_dishes)

print(famous_dishes.keys())

print(famous_dishes.values())
