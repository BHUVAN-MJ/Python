
# 3.Operators, Variables & Conditionals

"""
  Write a Python program that:
    1.Asks the user to input the total number of pizza slices they have, and the number of people eating (as integers).
    2.Calculates exactly how many slices each person gets using integer division (//).
    3.Calculates how many slices are left over using the modulo operator (%).
    4.Uses conditional logic to print: "Perfect split!" if there are no leftovers, or "X slices remaining." if there are.
      
"""

pizza_slices =int(input("Enter the pizza slices:"))
no_of_people =int(input("Enter the people number:"))

slice_that_each_gets = pizza_slices // no_of_people 
left_pizza_slice = pizza_slices % no_of_people


print("Each person gets:", slice_that_each_gets, "slices")


if left_pizza_slice == 0 :
    print("Perfect split!")
else:
    print(left_pizza_slice,"slice that left")


