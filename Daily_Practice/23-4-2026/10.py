
# 10.Mixed Loops (For inside a While!)

"""

  Write a Python program that:
    1.Sets play_again = "yes".
    2.Uses a while loop that runs as long as play_again == "yes".
    3.Inside the while loop, use a for loop with range(3) to print "Loading..." three times.
    4.After the for loop finishes, ask the user "Type 'yes' to play again: " and update the play_again variable.

      
"""

play_again ="yes"

while play_again == "yes":
    for i in range(3):
        print("Loading...")

    word =input("Type 'yes' to play again:").lower()
    play_again = word
