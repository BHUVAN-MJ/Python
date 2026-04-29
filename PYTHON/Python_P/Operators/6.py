#Operators 

#1.Assignment operators

x=5 #Assign 5 ot the variable x
print(x)

x+=3
print(x)

x-=2
print(x)

x*=5
print(x)

x/=3
print(x)


#2.Comparison operators

a=50
b=25

print(a==b) #Equal
print(a!=b) #Not Equal
print(a>b) #Greater
print(a<b) #Lesser
print(a>=b) #Greater or Equal
print(a<=b) #Lesser or Equal


#3.Logical operators

a=52
b=60
c=45

print(a<b and b>c)
print(c<40 or c>b)
print(not(c>b))


#Membership operators

string1=[1,2,3,5,6]
string2="Engineering"

print( 8 in string1)
print(5 not in string1)

print("a" not in string2)
print("e" in string2)

#Bitwise Operators

a=5
b=3

print(a&b) #bitwise AND
print(a|b) #Bitwise OR
print(a^b) #Bitwise XOR
print(~a) #Bitwise NOT
print(a<<b) #Bitwise Left Shift
print(a>>b) #Bitwise Right Shift

#Arithmetic operators

a=25
b=6

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**3)
