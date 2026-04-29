# Tuples And Sets in Python

my_tuple=("apple","banana","kiwi","mango","cherry") #this is a tuple

single_tuple=("apple",) # when we write a single tuple we have to use a comma

# Accessing tuples

fruits=("apple","banana","kiwi","cherry")
print(fruits[1]) # here we are using index to print the value 
print(fruits[-1]) # here we are using index to print the value 


#slicing tuples

print(fruits[0:3]) #here we using start:stop:step to slici the tuples

#Tuple opreations

# tuple concatention

tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2) # here we using + opreator to add to tuples

#tuple repetition

repeated_tuple=(1,5,3)*4
print(repeated_tuple) #here we using * opreators to multipli the tuple

#checking Membership

print("apple" in fruits) # here we using in function to check if the value is in the tuple
print("mango" not in fruits) # here we using not in function to check if the value is in the tuple

#Tuple methos

print(my_tuple.count("apple")) #here we are using the count() method to check the number of the values
print(tuple1.count(1))
 
print(my_tuple.index("kiwi")) #here we  are using index() to check the index number of a value


# Sets 

my_sets={"apple","banana","kiwi","cherry","mango"}
numbers_set={1,5,6,2,3,4,5,8}

# empty set

empty_set=set()

# Set operations

# union

set1={1,2,3,4} 
set2={4,5,6,7}
union_set=set1 | set2 #her when we use | set union the opreation removes the duplicate
print(set1 | set2)

# Intersection 

intersection_set=set1 & set2 
print(intersection_set) #here the & intersection only print the set that common in both sets

# Difference

difference_set=set1 - set2
print(difference_set) # here - this opretor return the sets on the frist set before the common value in both set

#Symmetric difference

sym_diff_set=set1 ^ set2
print(sym_diff_set) # here ^ this function removes the elements that are common

#Set methods 

my_sets.add("orange") #here using add() we can add an element to the set
print(my_sets) 

my_sets.remove("kiwi") #here remove() removes an element if its in the set if not it shows an error
print(my_sets)

my_sets.discard("kiwi")  #here discard() removes an element if its in the set if not it will not shows an error
print(my_sets)

a= my_sets.pop() #here pop() it will remove a random set value
print(my_sets)
print(a) # with assing it to a variable we can see the value that has been removed

set_1={"name","what","you"}
set_1.clear() # here clear() will remove all the elements in a set
print(set_1)
