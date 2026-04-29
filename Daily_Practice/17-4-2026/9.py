
# 9.For Loop, Dictionary & Conditionals

"""
  Write a Python program that:
    1.Creates a dictionary of test scores: {"John": 45, "Sara": 80, "Mike": 55}.
    2.Uses a for loop to iterate through the dictionary keys.
    3.If the dictionary value for that key is greater than 50, print that the person "Passed".

      
"""

scores = {
    "John":45,
    "Sara":80,
    "Mike":55
}

for name in scores :
    if scores[name] > 50:
        print(f"{name} Passed")

      