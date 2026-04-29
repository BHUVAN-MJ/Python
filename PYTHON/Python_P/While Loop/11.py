# While loops

"""
1.Let's print numbers from 1 to 5 using a while loop

"""

i=1

while i<=5:
    print(i)
    i+=1

"""
2.let's relate this to a common exampleimagine your counting sheep to fall asleep

"""

sheep_count=1
while sheep_count<=10:
    print(f"sheep{sheep_count}")
    sheep_count += 1

# Avoiding in loops
 
"""
 An infinite loop

i=1
while i<=5:
    print(i)
    break

"""
# using break to exit a while loop

"""
let's stop counting sheep afther 5 sheep even though the condition allows counting up 10:

"""
sheep_count = 1
while sheep_count <= 10:
    print(f"sheep{sheep_count}")
    if sheep_count == 5:
        print("That's enough counting:")
        break
    sheep_count += 1


# Using continue to skip an Iteration 

"""
Let's say you want to skip counting sheep that are number 4:

"""
sheep_count1 = 1
while sheep_count1 <= 5:
    if sheep_count1 == 4:
        sheep_count1 += 1
        continue
    print(f"sheep{sheep_count1}")
    sheep_count1 += 1

# using while loops for user Input

"""
you can use a while loop to repeatedly ask the users for input until they enter the correct one
"""

pin = "  "
correct_pin = "1234"

while pin != correct_pin:
    pin = input("Enter your PIN: ")
    if pin != correct_pin:
        print("Incorrect PIN,Try again")
print("PIN accepted,you can proceed")
