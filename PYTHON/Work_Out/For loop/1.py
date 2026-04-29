# Write a for loop that prints all multiples  tables of 3 between 1 and 30.

for i in range(3,31,3):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print()

