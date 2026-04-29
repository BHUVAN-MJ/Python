# Tuple and Set Comparison:

"""

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?

"""
#Create a list of elements and convert it into both a tuple and a set.

my_list=[20,56,6,85,35,65,41]
print(my_list)
print(type(my_list))

my_tuple=tuple(my_list)
print(my_tuple)
print(type(my_tuple))

my_set=set(my_list)
print(my_set)
print(type(my_set))

#Print both the tuple and the set

print(my_tuple)
print(my_set)

#Try to add new elements to the tuple and set. What differences do you observe?

# in tuple
"""
my_tuple.append(21)
print(my_tuple)

"""

#in set

my_set.add(59)
print(my_set)