"""
Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 5_8_4
    Description of Problem (just a 1-2 line summary!):Prompt for a file name of
    text words.  Read the file and convert the words to a list.   Call a function
    you created called list_to_words(), that takes a list as an argument and
    returns a list that contains only words that occurred once in the file.  
"""
import sys

def list_to_words(word_list):
    """takes a list as an argument and returns a list that contains only
    words that occurred once """

    temp_list = []
    # get word count
    for j in word_list:
        temp_list.append(word_list.count(j))
    # only take words with count of 1
    final_list = [x for x in word_list if word_list.count(x) == 1]

    return final_list

if __name__ == '__main__':
    # while loop until input is correct
    i = 1
    while i == 1:
        try:
            # accept and access filename with extension
            file_name = input("Please enter only your file name with "
                              "extension see example (ex. file.txt): ")
            new_list = []
            with open(file_name, 'r') as file:
                new_list = file.read().split()
            # close file and end loop
            file.close()
            i = 0
        # catch errors and continue loop
        # if two errors thrown prevent crash by exiting

        except (FileNotFoundError, NameError) as error:

            print("FileNotFoundError: Incorrect file name or "
                  "file does not exist!")
            sys.exit()
        # else only one error

        except FileNotFoundError:
            print("FileNotFoundError: Incorrect file name or "
                  "file does not exist!")
            file.close()
            i = 1
            continue
        except NameError:
            print("Name error!")
            file.close()
            i = 1
            continue
        except IndexError:
            print("Index error!")
            file.close()
            i = 1
            continue


        # try to run function with supplied list from text file
        try:
            print("These are the words in your text file that appear once: "
                  , list_to_words(new_list))
            # if successful end loop and ensure file is closed
            i = 0
            file.close()
        # handle errors
        except NameError:
            print("Name Error!")
            i = 1
            file.close()


