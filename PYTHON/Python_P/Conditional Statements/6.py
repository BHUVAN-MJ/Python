# Example: Checking Bus Ticket Prices

"""
Let’s create an example based on ticket prices for a Karnataka KSRTC bus. 
If the passenger is under 5 years old, the ticket is free. 
If the passenger is between 5 and 12 years old, they get a child discount. 
If the passenger is 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full fare.

"""
age_3=20

if age_3<=5:
    print("The bus ticket is free!.")
elif age_3>5 and age_3<=12:
    print("you get a child discount!.")
elif age_3>=60:
    print("you get a senior citizen discount.!")
else:
    print("You have to pay full price.")