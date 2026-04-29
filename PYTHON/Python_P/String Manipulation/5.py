#String Manipulation 

frist_name="Naveen"
last_name="Kumar"
full_name=frist_name+" "+last_name
print(full_name)


#Repetition

message="I Love Money!\n "*100
print(message)


#String Methods

statement=" There are somethings that have to be done. "
print(statement.upper())
print(statement.lower())
print(statement.strip())
print(statement.replace("done","  "))

#Accessing string

text="Hey you there!" #here the index start with 0 
print(text[2])
print(text[8])
print(len(text))

#Slicing string

print(text[0:13]) #here the position-1 to get the index number of a word\letter
print(text[:-1:2])
print(text[1::5])

#Escape Sequences

print("Hey you there,\n How are you!")
print("1 \t 2")
print("1\\2")