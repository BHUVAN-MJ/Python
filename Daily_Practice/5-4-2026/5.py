"""

1]. **Character Counter**:
   Write a Python program that:
   - Asks the user for a string.
   - Prints how many characters are in the string, excluding spaces.

   **Example**:
   
   python
   Input: "Hello World"
   Output: "Number of characters (excluding spaces): 10"
   
 """

string = input("Enter a string:")
no_of_chara = len(string.replace(" ",""))
print("No of characters (excluding space):",no_of_chara)