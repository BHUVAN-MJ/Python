"""

1. **Logical Operator Practice**:
   Write a Python program that takes two numbers as input from the user and checks if:
   - Both numbers are greater than 10 (using `and`).
   - At least one of the numbers is less than 5 (using `or`).
   - The first number is not greater than the second (using `not`).


"""

a = int(input("Enter frist number:"))
b = int(input("Enter second number:"))

print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>b))