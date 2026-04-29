# List in python

fruits=["apple","banana","grapse","kiwi","mango"] #lists of strings
numbers=[1,5,6,3,4,5,6,7] #lists of numbers
mixed=["pen","rock",2,5,6,3,True,False] #list that include numbers,bollean,string

print(fruits)
print(numbers)
print(mixed)

# Accessing List element

print(fruits[2])  #in python index start from the number 0 
print(numbers[3])

# we can also use the negative numbers as index

print(mixed[-5])


# Modifying the list

#changing a specific element
fruits[-1]="orange"
print(fruits)

# Adding elements

numbers.append(8) # here we used the append(). append() adds an element to the end of the list
print(numbers)

mixed.insert(3,"me") #here we are using the insert().insert adds an element to a specific index
print(mixed)


# Removing a elelment

mixed.remove("me")
print(mixed)

numbers.pop(3)
print(numbers)

fruits.clear()
print(fruits)

# Slicing lists

#[start:stop:step]

numbers_1=[1,5,6,7,8,9,32,15,63,42,35]
print(numbers_1)

print(numbers_1[0:6]) #slicing the list from 0 index to 6 th index

print(numbers_1[3:]) #slicing the list from index 3 to end of the list

print(numbers_1[::2]) #slicing the list from the start to end but skiping 2 indexs


# list functions

print(len(numbers)) # here we using the len() function to count the lenth of the list

print(sorted(numbers_1)) #here we using the sorted() function to sort the numbers in assending order by default

print(sum(numbers_1)) #here we using sum() function to add the numbers in the list

# list methods

print(numbers_1.index(15)) #here we using the index() method to count the index of the value

mixed.reverse() #here we using the reverse() to reverse the list 
print(mixed)

print(numbers.sort()) # here we using the sort() to sort the list by assending or dessending order
print(numbers)

# Nested lists 

matrix=[[1,2,5],[6,3,7],[7,8,6]]
print(matrix[0]) # here it take the [1,2,5] as index 0
print(matrix[0][2]) #here in index 0 we printing the 2 index in the matrix
