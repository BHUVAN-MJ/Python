
# 5.Dictionary Updating & Conditional Logic

"""
  Write a Python program that:
    1.Creates a simple shopping cart dictionary: {"shoes": 50, "shirt": 20}.
    2.Prompts the user for a discount code.
    3.Uses a conditional statement to verify if the code entered matches "HALFOFF". 
    4.If it matches, use dictionary value modification and division to cut the prices of both items exactly in half, 
     then print the updated cart dictionary.
      
"""

shoping_cart ={
    "shoes":50,
    "shirt":20
}

discount_code =input("Enter a discount code:").upper()

if discount_code == "HALFOFF":
    for item in shoping_cart :
      shoping_cart[item] =shoping_cart[item] / 2
      print("The price after the discount:",shoping_cart)
else:
    print("Enter the valid discount code!")


"""

shopping_cart = {
    "shoes": 50,
    "shirt": 20
}

discount_code = input("Enter a discount code: ").upper()

if discount_code == "HALFOFF":
    shopping_cart["shoes"] = shopping_cart["shoes"] / 2
    shopping_cart["shirt"] = shopping_cart["shirt"] / 2

    print("Prices after discount:", shopping_cart)
else:
    print("Enter a valid discount code!")


"""