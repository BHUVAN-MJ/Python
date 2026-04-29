
# 2.Iterate over a list

"""
  Write a Python program that:
    1.Create a list of five countries.
    2.Use a for loop to print each country with its index number (starting from 1).
    3.Print the country name in uppercase on the same line.
 
      
"""


countries =["USA","UK","UAE","INDIA","RUSSIA"]

for index , country in enumerate (countries,start=1):
  print(f"{index}.{country.upper()}")