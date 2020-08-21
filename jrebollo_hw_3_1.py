
"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 7/29/20
Homework Problem 1
Description of Problem (just a 1-2 line summary!): Write a Python program that counts the number of odd numbers,
even numbers, squares of an integer and cubes of an integer from 2 to 130 (inclusive).
"""

# constants
START = 2
END = 131

# list that contains the whole range
num_list = []
for i in range(START, END):
    num_list.append(i)

print("Printing the whole list:")
print(START, END-1)


# counts evens
even_list = []
for num in range(START, END):
    if num % 2 == 0:
        even_list.append(num)
print("Printing evens: ")
print(even_list[0],"....",  even_list[-1])
print("Count of Evens: " , len(even_list))

# counts odds
odd_list = []
for num in range(START, END):
    if num % 2 == 1:
        odd_list.append(num)
print("Printing odds: ")
print(odd_list[0], "....", odd_list[-1])
print("Count of odds : " , len(odd_list))

# counts square
square_list = []
for squ in range(START, END):
    if (squ **(.5)) == int(squ **(.5)):
        square_list.append(squ)
print("Printing squares: ")
print(square_list)
print("Count of Squares: " , len(square_list))

# counts cubes
cube_list = []
for cub in range(START, END):
    root = round(float(cub **(1/3)))
    if (root * root * root) == cub:
        cube_list.append(cub)
print("Printing cubes: ")
print(cube_list)
print("Count of Cubes: " , len(cube_list))

