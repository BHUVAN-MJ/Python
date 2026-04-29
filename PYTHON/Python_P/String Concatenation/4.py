# String Concatenation 

boy_name= input("Boy Name: ")
boy_age=int(input("Boy Age: "))
 #int used because the boy_age when we input a input it always be a string 
girl_name= input("Girl Name: ")
girl_age= int(input("Girl Age:"))
 #int used because the girl_age when we input a input it always be a string 

print(boy_name)
print(girl_name)

age_diff= abs(boy_age-girl_age) 
#here abs means abslute value because we don't kwon the age diff.it can be negative int also 

print(age_diff)
print(boy_name+ " Loves " +girl_name)

print(boy_name + " loves "+ girl_name + ". The age diffrence is "+ str(age_diff)) 
#here we used the str to convert the age_diff variable from the int to str


"""
Using the f{} string 
"""

print(f"{boy_name} Loves {girl_name}. Age diffrence is {age_diff}")