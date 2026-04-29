
# 3.List Manipulation & Operators

"""
  Write a Python program that:
    1.Initializes a list with three preset movie titles.
    2.Prompts the user to enter a new movie title.
    3.Uses an operator (like +) or a list method to combine the new movie into the existing list.
    4.Modifies the list so the first item in the list becomes the string "Classics". 
      
"""

movies = ["Dude","With love","Dragon"]

New_movie = input("Enter the new movie:")

movies.append(New_movie)
# movies = movies + [New_movie]
movies[0] = "Classics"

print("Update movies:",movies)



