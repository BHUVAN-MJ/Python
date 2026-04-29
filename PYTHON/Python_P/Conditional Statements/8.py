
# The match-case Statement (Python 3.10+)

"""
Let’s check the type of day using match-case

"""

day = "Sunday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday.")