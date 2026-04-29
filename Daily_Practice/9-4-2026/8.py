
# 8.Operators, List & Conditionals

"""
  Write a Python program that:
    1.Takes a single mathematical integer as an input (e.g., total points scored).
    2.Calculates the remainder of this integer when divided by 2 using the modulo operator.
    3.Uses an if-else statement to print whether the scored points are an "Even" or "Odd" number. 
      
"""

Total_score = int(input("Enter the total score:"))

remainder = Total_score % 2
print(remainder)

if remainder == 0:
    print("The Total score is even")
else:
    print("The Total socre is odd")