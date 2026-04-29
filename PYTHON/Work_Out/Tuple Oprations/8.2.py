# Set Operations:

"""

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?

"""
#Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.

my_fav_fruits={"mango","apple","grapes","banana"}
your_fav_fruits={"kiwi","apple","orange","guva","jack fruit"}

print(my_fav_fruits)
print(your_fav_fruits)

#Find the union, intersection, and difference between the two sets.

union_fruits=my_fav_fruits | your_fav_fruits
print(union_fruits)

intersection_fruits=my_fav_fruits & your_fav_fruits
print(intersection_fruits)

difference_fruits=my_fav_fruits - your_fav_fruits
print(difference_fruits)

#Add a new fruit to your set.

my_fav_fruits.add("kiwi")
print(my_fav_fruits)


#Remove a fruit from your set using both remove() and discard(). 

my_fav_fruits.remove("kiwi")
print(my_fav_fruits)

your_fav_fruits.discard("banana")
print(your_fav_fruits)

# What happens when the fruit doesn’t exist?
"""
When we use remove() it will show an error.but
when we use discard() it will not show an error
"""