
# 8.Nested Dictionaries & Conditionals

"""
  Write a Python program that:
    1.Creates a nested dictionary containing stats for two different cars:
    2.cars = {"Mustang": {"price": 40000, "color": "Red"}, "Civic": {"price": 25000, "color": "Blue"}}.
    3.Asks the user which car they want to check out.
    4.Uses conditional logic to check if their input exists as a key in the cars dictionary.
    5.If it does, extract and print just the price. If not, print "Car model not found."

      
"""

cars ={
    "mustang":{
        "price":40000,
        "color":"red"
    },
    "civic":{
        "price":25000,
        "color":"blue"
    }
}

car_name =input("Enter the car name you want:")

car_name =car_name.strip()

if car_name in cars.keys():
    print("price:",cars[car_name]["price"])
else:
    print("car model not found")

