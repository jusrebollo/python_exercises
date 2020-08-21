"""Justin Rebollo
    Class: CS 521 - Summer 2
    Date: 7/29/20
    Homework Problem 4
    Description of Problem (just a 1-2 line summary!):Write a program to:print all the keys. print all the values.print all the keys and values pairs.print all the keys and values pairs in order of key.print all the keys and values pairs in order of value.

"""
# provided dict
my_dict = {'a': 15 , 'c': 18 , 'b': 20}

# temp to hold iterable keys
temp = my_dict.items()
# sorted keys
sorted_key = sorted(temp)

# sorted values with lambda , reusing temp
sorted_value = sorted(temp, key = lambda x: x[1])

# print as instructed
print("Keys: " , my_dict.keys())
print("Values: " , my_dict.values() )
print("Pairs: " , my_dict.items())
print("Dictionary sorted by key: " , sorted_key)
print("Dictionary sorted by value: " , sorted_value)

#confirm output is ok ??????
