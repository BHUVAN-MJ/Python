
# 6.For Loop, Variables & Operators (The Accumulator)

"""
  Write a Python program that:
    1.Creates a variable total = 0 and a list of expenses: [15, 20, 5].
    2.Uses a for loop to go through the list.
    3.Adds each expense to the total variable. Print the total outside the loop once it finishes.

      
"""
total =0

expenses =[15,20,5]

for i in expenses :
    total += i
print(total)