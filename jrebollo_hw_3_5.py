"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 7/29/20
Homework Problem 5
Description of Problem (just a 1-2 line summary!): Create a test file with a single sentence of 20 words.   Read the file, insert appropriate new line characters (\n)
and write the test to a new text file that contains four lines of five words.  
"""

import os.path
from os import path

#open file
if path.exists("jrebollo_hw3_test_1.rtf"):
    file = open("jrebollo_hw3_test_1.rtf", "r" )
    print("Successful file opening!")
else:
    print("Error opening file!")

#create output file
new_file = open("new_file.rtf", "w")

file_data = file.read()
words = file_data.split()

#if initial file is not 20 words program ends
if (len(words)) != 20:
    print("Error: Your file is not twenty words!")
    file.close

#creates the 5 lines of 4 words
else:
    updated_text = ""
    count = 0
    for i in words:
        updated_text += i + " "
        count += 1
        if count == 5:
            updated_text += "\n"
            count = 0

    new_file.write(updated_text)

    file.close
    new_file.close



