
# 7.While Loop & Input Validation (Conditionals)

"""
 Write a Python program that:
    1.Sets a variable age = -1.
    2.Uses a while loop that runs as long as age is less than 0.
    3.Inside the loop, prompt the user to enter their age (as an integer). If they type a negative number, it will naturally loop again!.
    4.Print "Valid age accepted" once the loop finishes.
      
"""

age = -1

while age < 0:
    age =int(input("Enter a age:"))
    
print("Valid age accepted")
