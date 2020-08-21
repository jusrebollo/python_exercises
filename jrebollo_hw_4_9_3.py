"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 8/5/20
Homework Problem 3
Description of Problem (just a 1-2 line summary!):Start with 2 lists. One with first names and another of last names.Use zip to create a dictionary with the keys as the last names and the values as the first names.

"""
# first name list
first = ['Jane', 'John', 'Jack', 'Justin']

# last name list
last = ['Doe', 'Deer', 'Black', 'Rebollo']

# zip
zip_list = zip(last, first)

# new dict
new_dict = dict(zip_list)

# print as instructed
print("First Names List: ", first)

print("Last Names List: ", last)

print("Dictionary of combined lists: ", new_dict)
