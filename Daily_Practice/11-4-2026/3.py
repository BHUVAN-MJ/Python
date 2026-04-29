
# 3.Tuples, Variables & Nested Conditionals

"""
  Write a Python program that:
    1.Prompts the user to enter a package's length, width, and height individually.
    2.Groups these three variables together into a single Tuple named dimensions.
    3.Uses mathematical operators to calculate the package's total volume.
    4.Uses conditional logic to classify the package: If the volume is greater than 1000, check if the weight (prompt the user for weight) 
     is over 50kg. If both are true, print "Heavy & Bulky Cargo".
      
"""



length =float(input("Enter lenght:"))
width =float(input("Enter width:"))
height =float(input("Enter height:"))

dimensions =(length,width,height)

volume = dimensions[0] * dimensions[1] * dimensions[2]

if volume > 1000 :
    weight =float(input("Enter the weight in(kg):"))

    if weight > 50 :
        print("Heavy & Bulky Cargo")
    else:
        ("Bulk but not heavy")
else:
    print("Normal pacage")
