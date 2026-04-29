# Nested if statement

"""
Let’s say you’re planning to visit Mysuru. 
You want to decide whether to go based on the day of the week and the weather.
"""

day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")