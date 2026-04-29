
# 8.While Loop, Conditionals & Operators

"""
  Write a Python program that:
    1.Sets a variable score = 0.
    2.Uses a while loop that runs while score < 50.
    3.Inside the loop, add 15 to the score each time, and use an if statement to print "Almost there!" if the score reaches 30.

      
"""
score =0

while score < 50:
    score += 15
    print(score)
    
    if score == 30:
        print("Almost there!")
