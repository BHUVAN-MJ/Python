
# 9.Escape Sequences, Strings & Dict Output

"""
  Write a Python program that:
    1.Creates a Dictionary representing flight details: Flight number, Origin, Destination, and Gate.
    2.Extracts each value from the dictionary into a formatted "boarding pass".
    3.Uses \n, \t, and manual string spacing (concatenation) to print an organized box-like output ticket over several formatted lines on the
      screen.

      
"""

flight ={
    "flight no":"A15",
    "origin":"banglore",
    "destination":"usa",
    "gate":"E1"
}

print("------------Boarding pass------------\n")

print("\t Flight NO:",flight["flight no"])
print("\t Origin:",flight["origin"])
print("\t Destination:",flight["destination"])
print("\t gate:",flight["gate"])

print("\n------------------------------------")