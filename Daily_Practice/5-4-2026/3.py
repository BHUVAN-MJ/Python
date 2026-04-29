"""
    **Simple Greeting Program**:
1]. Write a Python program that asks the user for their name and age, 
   then prints a personalized greeting message. Use both the `+` operator and f-strings for output.

    **Example**:
    python
    Enter your name: Alice
    Enter your age: 25
    Output: Hello, Alice! You are 25 years old.
   
   """

#Using The + operator


User_name = input("Enter your Name:")
User_age = int(input("Enter your age:"))

Greetings = " Hello,  "    +   User_name   +   "  You are  "  +  str(User_age)  +  "  years old.  "

print(Greetings)

# Using f-string

Greeting = f" Hello, {User_name}. you are {User_age} years old."
print(Greeting)


