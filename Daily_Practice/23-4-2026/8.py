
# 8.For Loop & Set

"""
  Write a Python program that:
    1.Creates a Set of vowels: {"a", "e", "i", "o", "u"}.
    2.Asks the user to type a single letter.
    3.Uses a for loop to go through the Set. If the user's letter matches the vowel in the loop, print "It's a vowel!".

      
"""

vowels ={"a","e","i","o","u"}

letter =input("Enter a single letter:").lower()

for let in vowels:
    if letter == let :
        print("It's a vowel!")

