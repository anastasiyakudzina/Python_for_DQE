import random
import string
from random import randint

# Creating an empty list.
mylist = []
# Defining a number of dicts (from 2 to 10).
# "Randint" returns a random integer in range [start, end] including the end points.
number_of_dicts = randint(2, 10)

# 26 letters in lowercase from ascii
letters = string.ascii_lowercase

# Using the "for" loop for iterating over the list and creating random number of dicts with key-value in the dicts.
for n in range(number_of_dicts):
    # Defining the dict's random numbers of keys that should be letter.
    # 26 letters: "abcdefghijklmnopqrstuvwxyz"
    list_length = randint(1, 26)
    # Using random.sample() functions to generate random number list
    # Value - "letters", length of list - "list_length".
    random_list = random.sample(letters, list_length)
    # Defining the dict's values that should be a number (0-100)
    res = {ele: randint(0, 100) for ele in random_list}
    # Adding a copy or the received dict with key-value in the "mylist"
    mylist.append(res.copy())

# Printing input result. The str() function converts the list into a string.
print("Input : \n" + str(mylist))

# Combining values of same keys in a list of dicts.
prepared_dict = {
    # Going through all elements in dict list and get values for current key "k"
    # Values include "None"
    k: [d.get(k) for d in mylist]
    # Getting all keys from list of dictionary and unite them distinctly by using set().union
    for k in set().union(*mylist)
}

# Printing intermediate result. The str() function converts the dict into a string.
print("\nIntermediate result : \n" + str(prepared_dict))

# Creating an empty list.
final_dict = {}

# Using the "for" loop for iterating over the dict with intermediate result and
for key, value in prepared_dict.items():
    # Finding "not None" values in the list with combined values of same keys
    not_none_values = [i for i in value if i is not None]
    # Finding max "not None" value in this list
    max_value = max(not_none_values)
    # Finding index of max "not None" value in this list
    max_index = value.index(max_value)
    # Key is only in one dict, if length "not None" value is equal to 1
    if len(not_none_values) == 1:
        # Don't add an index to the key name
        final_dict[key] = max_value
    # Else dicts have same key
    else:
        # Taking max value, and renaming key with dict number with max value
        final_dict[key + '_' + str(max_index + 1)] = max_value

# Printing final result. The str() function converts the dict into a string.
print("\nFinal result : \n" + str(final_dict))
