
"""

1. **List Manipulation Exercise**:
   - Create a list of 5 items (strings or numbers).
   - Add a new item to the end of the list and another at the second position.
   - Remove the third item from the list.
   - Print the list after each operation.


   """

List = [5,6,7,8,9,10,31]
print("The original :",List)

List.append(9)
print("After adding a item at the end:",List)

List.insert(1,55)
print("adding a item at the second position:",List)

List.pop(2)
print("Removing the third item form the list:",List)