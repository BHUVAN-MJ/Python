
# 7.Number classifier loop

"""
 Write a Python program that:
    1.Loop through a list of 10 numbers.
    2.For each number print Positive, Negative, or Zero.
    3.Also print the largest number found after the loop.


"""

numbers =[0,1,2,5,-8,6,-4,-90,0,2]

largest = numbers[0]

for num in numbers:
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    elif num == 0:
        print(f"{num} is Zero")

for num in numbers:
    if num >largest :
        largest =num
    
print(f"{largest} is largest number")