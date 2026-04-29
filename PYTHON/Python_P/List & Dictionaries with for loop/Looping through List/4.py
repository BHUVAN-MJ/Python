# Adding marks to students using index values 

students = ["Anand","Kumar","Geetha"]
marks = [85,90,86]

student_marks = {}

for i in range (len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)
