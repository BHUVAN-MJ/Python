
# 9.Nested Dicts & Variables

"""
  Write a Python program that:
    1.Prompts the user to type in a single word.
    2.Extracts the city from the dictionary into a separate variable.
    3.Capitalizes the city variable using string manipulation and replaces the value back into 
      the nested dictionary. 
      
"""

word = input("enter a word:")

data ={
    "user":{
        "name":word,
        "city":"benglore"
    }
}

city = data["user"]["city"]
city = city.upper()

data["user"]["city"] = city

print("updated data:",data)