
# 4.For Loop & Tuple

"""
 Write a Python program that:
    1.Creates a Tuple of temperatures: (72, 85, 90, 65).
    2.Uses a for loop to check each temperature.
    3.Prints "Too hot!" if the temperature is over 80.
       
"""

temperatures =(72,85,90,65)

for temp in temperatures:
    if temp > 80:
        print(f"{temp} Too hot!")

