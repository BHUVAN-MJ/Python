"""
You are given a code which gets as input a number that indicates the temperature in Celsius and stores it in a variable named temperature.

Note: Don't modify the first line of the code.

 

Your task is to set the value of the weather variable based on the following conditions:

    "Freezing" if temperature is below 0,
    "Cold" if temperature is between 0 and 15 (including 0 and 15).
    "Mild" if temperature is between 16 and 25 (including 16 and 25)
    "Hot" otherwise

"""

temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below

if temperature <0:
    weather ="Freezing"
elif temperature >0 and temperature <=15:
    weather ="Cold"
elif temperature >16 and temperature <=25:
    weather ="Mild"
else:
    weather ="Hot"
# Don't change the line below
print(f"weather = {weather}")