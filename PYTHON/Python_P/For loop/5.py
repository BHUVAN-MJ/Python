# Using break in a for loop

"""
Stop the loop when you find specific item

"""
# let's say you are searching for a specific city in cities

cities = ["Bengaluru","Hubballi","Hassan","Mangaluru","Mysuru"]
for city in cities:
     if city == "Mangaluru":
          break
print("city Found")
