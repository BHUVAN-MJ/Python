
# 10.Complex Logical Operations & Nested Conditionals

"""
  Write a Python program that:
    1.Assumes an account has a balance of $1000 and a daily withdrawal limit of $300.
    2.Prompts the user for a withdrawal amount.
    3.Checks if the withdrawal is above 0. If yes, it proceeds to check if the amount exceeds the daily limit.
    4.If the limit check is passed, check if the balance covers the withdrawal. 
      Deduct the money and show the new balance if all conditions pass.
      
"""

balance = 1000
withdrawal_limit = 300

amount =float(input("Enter the amount:"))

if amount > 0:
    if amount <= withdrawal_limit:
        if amount <= balance:
            balance = balance - amount
            print("Withdra succssful")
            print("The new balance:",balance)
        else:
            print("Insufficient balance")
    else:
        print("Amount exceeds daily limit")
else:
    print("invalid amount")
