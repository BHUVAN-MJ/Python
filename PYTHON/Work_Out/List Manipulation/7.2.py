"""

Reverse and Sort a List: 

Create a list of numbers and:

Sort it in descending order.
Reverse the sorted list and print it.

"""

lists=[1,2,8,6,4,5,12,7,9]
print(lists)

lists.sort(reverse=-1)
print(lists)

lists.sort(reverse=True)
print(lists)

lists.reverse()
print(lists)
