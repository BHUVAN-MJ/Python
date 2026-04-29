
# 10.While Loop & Mixed Logic

"""

  Write a Python program that:
    1.Asks the user to enter a number (as an integer).
    2.Uses a while loop that runs as long as the number is ODD (using modulo % 2 != 0).
    3.Inside the loop, print "That is odd, try again:" and ask for a new number.
    4.Print "Thank you for the even number!" when the loop successfully ends.
      
"""

num =int(input("Enter a number:"))

while num % 2 !=0:
    print("That is odd,try again")

    num =int(input("Enter a new number:"))

print("Thank you for the even number!")


