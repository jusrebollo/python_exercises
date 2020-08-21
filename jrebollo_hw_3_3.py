"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 7/29/20
Homework Problem 3
Description of Problem (just a 1-2 line summary!): Write a program that prompts the user for a sentence and calculates the number of uppercase letters,
lowercase letters, digits, and punctuation. Output the results neatly formatted and labeled in columns.
"""

import string

sentence_input = input('Please enter a sentence: ')

lower_count = 0
upper_count = 0
digit_count = 0
punct_count = 0

punct = string.punctuation

#counts character type
for i in sentence_input:
    if (i.islower()):
        lower_count += 1
    if (i.isupper()):
        upper_count += 1
    if(i.isdigit()):
        digit_count += 1
    if(i in string.punctuation):
        punct_count += 1

print("Upper" , "Lower" , "Digit" , "Punct")
print("-----", "-----", "-----", "-----")
print("%-5s %-5s %-5s %-5s" % (upper_count, lower_count, digit_count, punct_count))




