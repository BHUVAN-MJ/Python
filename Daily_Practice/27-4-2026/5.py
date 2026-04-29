
# 5.Filter a list with a loop

"""
  Write a Python program that:
    1.Create a list of 8 integers (mix of positive and negative).
    2.Use a loop to collect only the positive numbers into a new list.
    3.Print the new list and its sum.

      
"""


list1 =[-8,9,6,-22,3,8,-2,3]
list2 =[]

for i in list1:
    if i > 0:
        list2.append(i)
  
print(list2)
print(f"The sum of new list {sum(list2)}")