"""Justin Rebollo
Class: CS 521 - Summer 2
Date: 7/29/20
Homework Problem 2
Description of Problem (just a 1-2 line summary!): Set a constant with an odd length string.  Confirm in code that the string is of an odd length.
Otherwise, print a relevant message for the user and end the program. 
"""

sentence_input = input('Please enter a sentence with no spaces after the final word: ')

SENTENCE = sentence_input

length = len(SENTENCE)

if len(SENTENCE) % 2 == 1:
    print("Full sentence: ")
    print('"{}"'.format(SENTENCE))

    print("Length of sentence: ")
    print(len(SENTENCE))

    print("Middle of sentence: ")
    middle = SENTENCE[length//2]
    print('"{}"'.format(middle))

    print("Start of sentence to before the middle:")
    print('"{}"'.format(SENTENCE[0:length//2]))

    print("From after the middle to the end of the sentence")
    print('"{}"'.format(SENTENCE[((length//2)+1): length]))

elif len(SENTENCE) % 2 == 0:
    print("Sorry your sentence has to be off an odd length!")
    print("Length: " , len(SENTENCE))