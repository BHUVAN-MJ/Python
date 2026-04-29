# Dictionaries

# creating a dictionary
karnataka_foods={
    "Bengaluru":"Bisi Bele Bath",
    "Mysuru":"Mysore pak",
    "Mangaluru":"Neer Dosa"
}

#Accessing Dictionary

print(karnataka_foods["Mysuru"]) 

print(karnataka_foods.get("Shivamogga","not found"))

# Adding an item

karnataka_foods["Shivamogga"]="kadubu"
print(karnataka_foods)

# Updating an item

karnataka_foods["Bengaluru"]="Ragi mudde"
print(karnataka_foods)


# Dictionary Method

print(karnataka_foods.keys()) #here using key() we can print all keys in the dictionary

print(karnataka_foods.values()) #here using values() we can print all values in the dictionary

print(karnataka_foods.items()) #here using items() we can print all the items in the dictionary

new_dishes={"Hubballi":"Girmit"}
karnataka_foods.update(new_dishes) #here using the update() to add an item to the dictionary
print(karnataka_foods)

#Removing an item

karnataka_foods1=karnataka_foods.pop("Mysuru") #here we using pop() to delete an item
print(karnataka_foods1)
print(karnataka_foods)

del karnataka_foods["Mangaluru"] # here we using del to delete an item
print(karnataka_foods)

karnataka_foods.clear() #here we using clear() to delete the dictionary 
print(karnataka_foods)

