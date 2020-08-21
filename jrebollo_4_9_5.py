"""Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 5
    Description of Problem (just a 1-2 line summary!):Create 3 functions with docstring:letter_counts(), most_common_letter(),string_count_histogram(). Write 3 print statements with appropriate descriptions 
"""


def letters_counts(word):
    """Takes a string as its argument and returns a dictionary
    of the letters as keys and frequency counts as values."""
    word = word.replace(" ", "")
    letters_dict = {}

    for i in word:
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1

    return letters_dict


def most_common_letter(word):
    """Takes a string as its argument and
    returns a string of the most common letter(s).
    This function calls letter_counts"""

    supplied_dict = letters_counts(word)

    max_letter = max(supplied_dict.values())

    max_string = (str([i for i, j in supplied_dict.items() if j == max_letter]))

    return max_string


def string_count_histogram(word):  # finish
    """takes a string as its argument and returns a list of the unique letters,
    with each letter being the repeated number of times it appears in the string.
    This function calls letter_counts()"""

    new_dict = letters_counts(word)
    histogram_list = []

    for i in (new_dict.keys()):
        histogram_list.append(i * new_dict[i])
    
    print("Histogram:")

    return histogram_list


if __name__ == '__main__':
    supplied_string = "hello world how are you today hhh"
    print("Count of letters: ", letters_counts(supplied_string))
    print("The most common letter(s):", most_common_letter(supplied_string))
    print('\n'.join(string_count_histogram(supplied_string)))
