
# 4.Set Operators & Input Validation

"""
 Write a Python program that:
    1.Prompts the user to input one ingredient they currently have in their kitchen.
    2.Checks if the user's input is a part of the required Set.
    3.If it is, use the .remove() or .discard() method to remove it from the Set, then print the updated Set to show what ingredient is still
      missing.

      
"""

ingredients ={"carrot","alu","chilli","onion"}

item =input("Enter a ingrediant name:").lower()

if item in ingredients :
    ingredients.remove(item)
    print(ingredients)
else:
    print("Item not in ingredients")