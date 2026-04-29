"""
  
2. Type Conversion
Write a Python program that:

Takes a number as input (string).
Converts it to integer and float.
Prints both converted values.

"""

num = input("Enter a number:")

int_num = int(num)
print("converting 'a' as a integer value:",int_num)
print(type(int_num))


float_num = float(num)
print(type(float_num))
print("converting 'a' as a float value:",float_num)