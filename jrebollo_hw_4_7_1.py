"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 8/5/20
Homework Problem 1
Description of Problem (just a 1-2 line summary!):
Given a constant list of integers in the range 1 to 10 inclusive, use list comprehension (no explicit loops) to:
find the sum of the even and odd integers in list L.
"""

# constant list
CONSTANT_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension to find sum of even
sum_even_l = [sum(i for i in CONSTANT_LIST if i % 2 == 0)]
# list comprehension to find sum of even
sum_odd_l = [sum(i for i in CONSTANT_LIST if i % 2 == 1)]

# print sums of odd and even
print("Provided list: " , CONSTANT_LIST)
print("Sum of even: ",  sum_even_l)

print("Sum of odd: ", sum_odd_l)

