# Write a program that counts how many vowels are in a given string using a for loop.

text =input("Enter a string:")
vowels ="aeiouAEIOU"
count =0

for char in text:
    if char in vowels:
        count += 1

print("Total vowels in text:",count)