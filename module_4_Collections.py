import random
import string
from random import randint


def create_dict(dict_length, key):
    random_list = random.sample(key, dict_length)
    res = {ele: randint(0, 100) for ele in random_list}
    return res


def list_of_dict(dicts_num, dict_length, key):
    mylist = []
    for n in range(dicts_num):
        mylist.append(create_dict(dict_length, key))
    return mylist


def merge_dictionary_list(dict_list):
    return {
        k: [d.get(k) for d in dict_list]
        for k in set().union(*dict_list)
    }


def common_dict(merge_dict):
    final_dict = {}
    for key, value in merge_dict.items():
        not_none_values = [i for i in value if i is not None]
        max_value = max(not_none_values)
        max_index = value.index(max_value)
        if len(not_none_values) == 1:
            final_dict[key] = max_value
        else:
            final_dict[key + '_' + str(max_index + 1)] = max_value
    return final_dict


length_of_dict = randint(1, 26)
number_of_dicts = randint(2, 10)
letters = string.ascii_lowercase

if __name__ == '__main__':
    list_with_dict = list_of_dict(number_of_dicts, length_of_dict, letters)
    dict_with_list = merge_dictionary_list(list_with_dict)
    combined_dict = common_dict(dict_with_list)

    print("Input : \n" + str(list_with_dict))

    print("\nIntermediate result : \n" + str(dict_with_list))

    print("\nFinal result : \n" + str(combined_dict))
