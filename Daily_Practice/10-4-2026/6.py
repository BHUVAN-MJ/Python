
# 6.List Indexing, String Methods & Output

"""
  Write a Python program that:
    1.Prompts the user for their First Name and Last Name as two separate variables.
    2.Extracts just the first letter (index 0) of the first name and the first letter of the last name.
    3.Combines them to create their "Initials".
    4.Forces the combined initials string to be entirely uppercase, and prints: "Your registered initials are: XX".
      
"""
first_name =input("Enter first name:")
last_name =input("Enter your last name:")

initials =first_name[0] + last_name[0]
initials =initials.upper()

print(f"Your registered initials are {initials}")