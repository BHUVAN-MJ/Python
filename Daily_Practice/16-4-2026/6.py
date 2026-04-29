
# 6.Conditionals, Operators & While Loop

"""
  Write a Python program that:
    1.Sets a variable balance = 100.
    2.Uses a while loop that runs while balance > 0.
    3.Inside the loop, subtract 30 from the balance. Use an if statement to print "Low balance!" if the balance drops below 40.

      
"""

balance = 100

while balance > 0:
    balance -= 30
    if balance < 40:
        print("Low balance")
