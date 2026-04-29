# While loop

"""
Write a program that simulates a bus ticket booking system. 
The bus has 8 seats. Each time a seat is booked, the available seats decrease.
When there are no seats left, the loop stops and displays a message saying "All seats are booked."

"""

total_seats_available = 8
seats_booked = 0

print("Welcome to Ticket booking platform!")
print(f"The seats available:{total_seats_available}")

while seats_booked < total_seats_available:
    choice = input("If you want to book a seat:(yes/no)").lower()

    if choice == "yes":
        seats_booked += 1
        seats_left = total_seats_available - seats_booked
        print(f"Seat booked successfully,seats available:{seats_left}")
    elif choice == "no":
        print("Okay,May be next time")
        break
    else:
        print("Invalid input,please type yes or no")

if seats_booked == total_seats_available:
    print("All seats booked!")
