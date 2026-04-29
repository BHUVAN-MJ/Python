
# 5.Dictionary & Escape Sequences

"""
  Write a Python program that:
    1.Creates a dictionary representing a user: { "username": "admin123", "role": "superuser" }.
    2.Prompts the user for a secret PIN.
    3.If the PIN is exactly "9999", add a new key "access_level" with the value "High" to the dictionary. 
    4.Print out the updated dictionary's contents onto three separate, indented lines using escape characters (e.g., \n and \t). 
      
"""

user ={
    "username":"admin123",
    "role":"superuser"
}

pin = input("Enter the secret pin:")

if pin == "9999":
    user["access_level"]="high"


print("/n updated user dictaionry:/n")
print("username:",user["username"])
print("user role:",user["role"])

if "access_level" in user:
    print("access:",user["access_level"])