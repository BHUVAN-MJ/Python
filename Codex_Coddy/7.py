"""
Write a code that initializes three variables, x, y and z with the values 15, 4, and 23 (respectively).

After that, initialize the following variables:

    w that will hold the remainder of x divided by y  
    v that will hold the remainder of z divided by x
    u that will hold the remainder of z divided by y
Use the % operator for modulo (remainder).

"""

# Type your code below

x = 15
y = 4
z = 23

w = x % y
v = z % x
u = z % y

# Don't change the line below
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
print(f"w = {w}")
print(f"v = {v}")
print(f"u = {u}")