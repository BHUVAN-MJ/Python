
# 6.List Index Manipulation & Operators

"""
  Write a Python program that:
    1.Starts with a list of 5 test scores (integers): [85, 90, 78, 92, 88].
    2.Prompts the teacher for a new score to replace the middle score (index 2).
    3.Calculates the difference between the highest index item (the final score) and the lowest index item (the first score).
    4.Appends this calculated difference as a new final item to the list, then prints it.
      
"""

scores =[85,90,78,92,88]

new_score =int(input("Enter new score for middel position:"))
scores[2] =new_score

difference =scores[-1] - scores[0]

scores.append(difference)

print("updated scores list:",scores)