#Nested Dictionary Practice (Simple for now):

"""

Create a dictionary to store details of two of your friends, including their names, favorite subject,
and favorite food.
Access and print the favorite food of one friend.

"""

friends={
    "friend1":{
        "name":"Ravi",
        "favorite subject":"maths",
        "favorite food":"kushka"
    },

    "friend2":{
        "name":"Naveen",
        "favorite subject":"science",
        "favorite food":"biryani"

    }
}

print(friends["friend2"]["favorite food"])