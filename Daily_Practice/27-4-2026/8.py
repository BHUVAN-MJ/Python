
# 8.Multiplication table

"""
  Write a Python program that:
    1.Ask the user for a number between 1 and 10.
    2.Use a for loop to print its full multiplication table (1×n through 10×n).
    3.Neatly align the output using string formatting.

      
"""

number =int(input("Enter the number between 1 to 10:"))

print(f"\n Multiplication Table for {number}")
print("-" * 25)

for i in range(1,11):
    print(f"{i:>2} x {number} = {i * number:>3}")



"""
num = int(input("Enter a number between 1 and 10: "))

print(f"\nMultiplication Table for {num}")
print("-" * 25)

for i in range(1, 11):
    print(f"{i:>2} x {num} = {i * num:>3}")

"""