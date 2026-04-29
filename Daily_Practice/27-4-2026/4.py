
# 4.Analyse a sentence

"""
 Write a Python program that:
    1.Ask the user to type a sentence.
    2.Count and print the number of words.
    3.Print the sentence reversed word-by-word (last word first).
 
      
"""




sentence =input("Enter a sentence:")

words = sentence.split()

print(f"Number of words: {len(words)}")

reversed_words ="".join(reversed(words))
print(f"Reversed sentence: {reversed_words}")