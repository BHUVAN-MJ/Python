"""
1]. Write a python program that swaps the values of two variables with and without using a thrid variable. 

"""

# Using a third variable 

a = 10
b = 20

print("before swaping")

print('a=',a)
print('b=',b)

temp = a
a = b 
b = temp

print("after swaping")

print('a=',a)
print('b=',b)

# With out using a third variable 

A = 50
B = 10

print("before swaping :")
print('A=',A)
print('B=',B)

A,B = B,A

print("after swaping:")
print('A=',A)
print('B=',B)