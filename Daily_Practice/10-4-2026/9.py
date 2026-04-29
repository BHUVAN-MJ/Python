
# 9.Mixed Data Types & Complex Logical Operators

"""
  Write a Python program that:
    1.Initializes three variables for a banking app: age = int, credit_score = int, and has_job = boolean (True/False). Set the boolean to True. Ask the user for the other two.
    2.Checks a compound condition using logical operators (and/or): To get a loan, the user must be strictly older than 18 AND have a credit score of 700 or higher.
    3.Or, if their credit score is between 600 and 699, they must also have a job (has_job == True) to get the loan. 
    4.Print whether the loan is "Approved" or "Denied". 
      
"""

age =int(input("Enter your age:"))
credit_score =int(input("Enter your credit score:"))
has_job =bool(input("Enter Yes or No :"))

if age > 18 and credit_score >= 700:
    print("Approved")
elif credit_score >= 600 and credit_score <= 699 and has_job == True:
    print("You can get a loan")
else:
    print("Denied")


"""

age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))

# Boolean fixed (always True as per question OR convert properly)
has_job = True  # as per instruction

# Loan conditions
if age > 18 and credit_score >= 700:
    print("Approved")

elif age > 18 and (600 <= credit_score <= 699) and has_job:
    print("Approved")

else:
    print("Denied")


"""