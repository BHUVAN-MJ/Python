
# 1.String Manipulation, List & Set Conversion

"""
  Write a Python program that:
    1.Prompts the user to type a sentence with some repeated words.
    2.Splits that sentence into a List of words (using string methods).
    3.Converts the List into a Set to automatically remove all the duplicates.
    4.Prints out how many words the user typed originally, and how many unique words there are.

"""

sentence = input("Enters a sentence that have repeated words:")

words =sentence.split()

unique_words =set(words)

print("Total words:",len(words))
print("unique words:",len(unique_words))