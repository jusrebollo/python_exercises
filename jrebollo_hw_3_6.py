"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 7/29/20
Homework Problem 6
Description of Problem (just a 1-2 line summary!): Create a text file containing student records by line and each record is of the format:
Tyrion Lannister, 1, 3.7
Write a program to read the file line by line and store all the records in lists or tuples.
"""

import os.path
from os import path

if path.exists("jrebollo_hw3_test_3.rtf"):
    file = open("jrebollo_hw3_test_3.rtf", "r")
    print("Successful file opening!")
else:
    print("Error opening file!")

student_data = []

# file_data = file.read()

for entry in file.readlines():
    data = entry.split()
    if (len(data)) != 0:
        student_data.append(data)

print(student_data)

file.close()

# is this correct?
# check if it exists

