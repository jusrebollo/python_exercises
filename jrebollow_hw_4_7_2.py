"""Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 8/5/20
    Homework Problem 2
    Description of Problem (just a 1-2 line summary!):
    Generate a new list with same number of elements as the original list such that each integer in the new list is the sum of its nearest neighbors and itself from the original list.

"""
# supplied constant list
CONSTANT_LIST = [10, 20, 30, 40, 50]

# new list created using sum and zip to iterate over list and sum neighbors
updated_list = [sum(i) for i in zip([0] + CONSTANT_LIST[:-1], CONSTANT_LIST, CONSTANT_LIST[1:] + [0])]

# print lists
print("Original list: " , CONSTANT_LIST)

print("Updated list: " , updated_list)
