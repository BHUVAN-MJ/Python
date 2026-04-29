
# 6.List Methods & Tuple Basics

"""
  Write a Python program that:
    1.Creates a Tuple containing a student's ID, Name, and Course.
    2.Initializes an empty List called system_records.
    3.Appends the entire Tuple to the system_records list.
    4.Modifies the record to insert an empty Dictionary as the second element of the system_records list. 
      
"""

student_details = ( 12345 , "Bhuvan" , "cse" )

system_records = []

system_records.append(student_details)

print(system_records)
print(type(system_records))

system_records.insert(1,{})

print("After inserting the empty dictionary",system_records)