# Tuple Operations:

"""

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.

"""
my_tuple=(1,5,2,6,3)
print(my_tuple)

# here in the tuple values are fixed so we can not change or modify the tuple values

print(my_tuple[1:3])

your_tuple=(8,9,7,5,6)
print(your_tuple)

our_tuple=my_tuple + your_tuple
print(our_tuple)