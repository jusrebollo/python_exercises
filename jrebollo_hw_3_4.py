"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 7/29/20
Homework Problem 4
Description of Problem (just a 1-2 line summary!): Write a program that prompts the user to enter a three-digit whole number
such that the digits are in ascending order and without duplicates.
"""
import string

#0 if input has not met criteria, 1 if input has met criteria
test = 0

#loops until the input is correct
while test ==  0:

    num_input = (input('Please enter a three digit whole number which has '
                          'digits in ascending order and has no duplicate digits '
                          'with no spaces: '))

    if "." in num_input:
        print("Enter a whole number!")
        continue

#create ascending string to check if input is ascending
    sort_check = sorted(num_input)

#convert sorted string to one sorted integer
    to_string = [str(num) for num in sort_check]
    join_int = "".join(to_string)
    new_int = int(join_int)

#create int value of input
    integer_num = int(num_input)

    if (float(num_input)) % 1 != 0:
        print("You must enter an integer")
        continue


    elif (len(str(num_input))) != 3:
        print("You must enter a three digit integer")
        continue

    elif (len(set(str(num_input))) < len(str(num_input))) == True:
        print("You must not have any duplicate digits!")
        continue

    elif integer_num != new_int:
        print("You must enter a number with ascending digits")
        continue

    else:
        print("Your number meets the criteria!")
        test = 1
        break

#fix for float value start