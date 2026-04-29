
# 8.Nested Dictionaries & String Modification

"""
  Write a Python program that:
    1.Initializes nested data for an RPG video game character: character = {"Hero": {"Health": 100, "Weapon": "Sword"}}.
    2.Uses variable assignment and dictionary referencing to change the character's weapon to "Fire Sword".
    3.Checks if the new weapon string contains the substring "Fire" (using an operator or method).
    4.If it does, directly update the "Health" value in the dictionary by adding +10 bonus points.

      
"""

character ={
    "hero":{
        "health":100,
        "weapon":"sword"
    }
}

character["hero"]["weapon"] = "fire sword"

if "fire" in character["hero"]["weapon"]:

    character["hero"]["health"] += 10 

print(character)
