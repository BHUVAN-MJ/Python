
# 3.Dictionary, While Loop & Operators

"""
  Write a Python program that:
    1.Creates a dictionary for a game character: {"health": 10}.
    2.Uses a while loop that runs as long as the character's health is less than 50.
    3.Inside the loop, add 10 to the health value in the dictionary and print the updated dictionary.
  
    
"""


character ={
    "health" : 10
}

print(character)

while character["health"] < 50 :
    character["health"] += 10
    print(character)