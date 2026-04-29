
# 7.Nested If statements & While Loop

"""
 Write a Python program that:
    1.Sets a variable attempts = 0.
    2.Uses a while loop that runs while attempts < 3.
    3.Asks the user for a PIN. If the PIN is "1234", print "Unlocked" and change attempts to 3 (to end the loop).
    4.Use a nested if to check: if the PIN is wrong AND attempts == 2, print "Account Locked". Don't forget to add 1 to attempts each loop!


"""

attemps = 0

while attemps < 3:
    pin =input("Enter the PIN:")
    
    if pin == "1234":
        print("Unlocked")
        attemps = 3
    else:   
        if attemps == 2:
            print("Account Locked")

    attemps += 1
