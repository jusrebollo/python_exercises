"""
Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 8/12/20
    Homework Problem 5_5_1
    Description of Problem (just a 1-2 line summary!):Write a python program
    that does the following:Calls function vc_counter() that: takes a string
    argument counts the number of vowels and consonantsin the string returns
    a dictionary of the counts, using the keys total_vowels and total_consonants
"""


def vc_counter(words):
    """ takes a string argument counts the number of vowels and consonants in
    the stringreturns a dictionary of the counts, using the keys total_vowels
    and total_consonants"""

    # create dictionary
    count = {'total_vowels': 0, 'total_consonants': '0'}

    # create vowels and consonants to check words against
    vowels = 'aeiouiAEIOU'
    consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
    j = 0
    k = 0

    words_sentence = words.split(' ')

    # count total vowels and consonants
    for x in words:
        if x in vowels:
            j += 1
        elif x in consonants:
            k += 1
    # put values in count dict
    count['total_vowels'] = j
    count['total_consonants'] = k

    return count


if __name__ == '__main__':

    # prompt while values are not correct
    i = 1
    while i == 1:

        # try to get input
        try:
            sentence = str(input("Please enter a sentence with no numbers or "
                                 "punctuation: "))
            i = 0
        except ValueError:
            print("Value Error: Please enter a sentence")
            i = 1
        except NameError:
            print("Name Error: Please enter a sentence with no numbers")

        # try to print values
        try:
            list_of_values = list(vc_counter(sentence).values())
            print("Total vowels in your sentence:", list_of_values[0])
            print("Total consonants in your sentence:", list_of_values[1])
            i = 0
        except ValueError:
            print("Value Error: Please enter a sentence")
            i = 1
        except NameError:
            print("Name Error: Please enter a sentence with no numbers")
            i = 1

