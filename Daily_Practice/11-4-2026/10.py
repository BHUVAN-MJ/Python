
# 10.Compound Boolean Logic & Complex Checking

"""

  Write a Python program that handles amusement park rides:
    1.Asks the user for three details: age (integer), height_in_cm (integer), and has_heart_condition (String "Yes" or "No").
    2.Uses a highly detailed if-elif-else statement to sort them into rides.
    3.For the Rollercoaster, the user must be exactly taller than 140cm, older than 12, AND not have a heart condition.
    4.Print an exact refusal message if any specific combination fails, or a "Welcome aboard!" if everything perfectly matches the boolean 
      logic.
      
"""

age =int(input("Enter you age:"))
height_in_cm=int(input("Enter your height in cm:"))
has_heart_condition =input("Enter yes / no :").lower()

print("For RollerCoaster:")

if height_in_cm <=140 :
    print("Sorry the height is at least have to be 140 CM")
elif age < 12:
    print("You have to be older than 12 years")
elif has_heart_condition == "yes":
    print("you have heart condition sorry")
else:
    print("Wlecome aboard!")