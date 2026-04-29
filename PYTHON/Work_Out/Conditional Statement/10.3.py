# Conditional statement

"""
Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership. If they are 60 or older, 
they get a senior citizen membership. 
Otherwise, they get a regular membership.

"""

age=17

if age<18:
    print("you can get a free membership!")
elif age>=60:
    print("you get a senior citizen membership!")
else:
    print("you get a regular membership!")