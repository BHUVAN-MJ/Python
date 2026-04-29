# While loop

# Real life example

"""
Let's say you want to simulate a KSRTC bus seat booking system.The bus has 5 available seat is booked,
the available seats decrease.

"""
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    Booking = input("Do you want to book a seat?(yes/no):").lower()

    if Booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")