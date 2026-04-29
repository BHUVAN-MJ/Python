"""

2. **Comparison Operator Challenge**:
   Create a Python program that asks the user for their age and prints:
   - "You are an adult" if the age is greater than or equal to 18.
   - "You are a minor" if the age is less than 18.
   - Use `>=` and `<` comparison operators.

"""


age = int(input("Enter your age:"))

if age>=18:
    print("You are an adult")
elif age<18:
    print("You are a Minor")
    