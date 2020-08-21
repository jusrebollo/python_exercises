"""Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 6
    Description of Problem (just a 1-2 line summary!):Create a program that prompts a user for a number,
    validates the number,  re-prompts on error,converts the number to words using a dictionary and prints out the words.   
"""
# dictionary for converting digit and related punctuation to words
d = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '.': 'point',
    '-': 'negative'
    }

# input
i = 0
while i == 0:
    num = (input("Please enter a negative or positive integer (no fractions) "
                "with no spaces after your input or commas:"))
# list for digits/punctuation to words
    str_num = str(num)
    words = []
#do not allow commas, print error and exit
    if ',' in num:
        print("Error: Must be a negative or positive int with no commas or fractions!")
        i = 0
        pass

    else:
        i = 1
#length of input as a string
        length = (len(str(str_num)))
#iterates through inout and converts digit or punctuation to a word
        for i in range(length):
            words = ' '.join(d[i] for i in str_num)
#print converted list
        print("Printing your integer converted to words: ", words)
