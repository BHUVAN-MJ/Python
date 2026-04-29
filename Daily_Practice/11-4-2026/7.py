
# 7.Multi-step Mathematical Operators & Conditionals

"""
 Write a Python program that:
    1.Acts as a currency conversion calculator. Set exchange rates as variables (e.g., usd_to_eur = 0.90).
    2.Asks the user how many US Dollars they have.
    3.Checks if the dollar amount is 0 or a negative number. If so, print "Invalid amount".
    4.If valid, calculates the converted total, deducts a flat 5 EUR exchange fee from the total, and prints the final result.
      
"""

usd_to_eur = 0.90
us_dollar = float(input("Enter the amount you want yo exchange:"))

if us_dollar <= 0:
    print("Invalid amount")
else:
    total = usd_to_eur * us_dollar 
    print("The total amount after deducting 5 eur for exchange fee:",total - 5 )