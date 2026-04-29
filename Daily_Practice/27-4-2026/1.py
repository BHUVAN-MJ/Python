
# 1.Count with a for loop

"""
  Write a Python program that:
    1.Use a for loop to print numbers 1 through 20.
    2.On each line, also print whether the number is even or odd.
    3.Count and print how many even numbers appeared after the loop ends.

"""

even_count = 0
 
for i in range(1,20):
    if i % 2 == 0:
        print(f" {i} -Even")
        even_count += 1
    else:
        print(f" {i} -Odd")

print("The number of even number appeared:",even_count)