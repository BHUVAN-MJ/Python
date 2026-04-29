
# 4.Set, While Loop & Input

"""
 Write a Python program that:
    1.Creates a Set of winning numbers: {7, 14, 21}.
    2.Sets a variable guess = 0.
    3.Uses a while loop that runs as long as guess is NOT in the winning Set.
    4.Inside the loop, prompt the user to guess a number (convert it to an integer). Print "You won!" when the loop ends.
      
"""

winning_number ={7,14,21}

guess = 0 

while guess not in winning_number :
    guess =int(input("Guess a number:"))

print("Youu won!")
