
# 7.Set & List Operations

"""
 Write a Python program that simulates a VIP club door:
    1.Creates a Set of invited guests: {"Alice", "Bob", "Charlie"}.
    2.Creates an empty List called arrived_guests..
    3.Prompts the user for a guest's name.
    4.If the name is in the Set, .remove() the name from the Set, append the name to the arrived_guests List, and print "Welcome!".
      If not, print "Not on the list!". 
      
"""

invited ={"alice","bob","charlie"}
arrvied =[]

guest_name =input("Enter guest name:")

if guest_name in invited:
    invited.remove(guest_name)
    arrvied.append(guest_name)
    print("Welcome!")
else:
    print("Not on the list!")

    