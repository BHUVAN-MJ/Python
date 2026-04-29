# conditional statement

"""
Write a program to check if someone is eligible for a bus pass. If they are below 5 years, 
the bus pass is free. If they are 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full price.

"""

age=61

if age<=5:
    print("The bus pass will be free!")
elif age>60:
    print("you get a senior citizen discount")
else:
    print("you will pay full price!")