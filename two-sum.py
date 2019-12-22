import math

def search(my_list):
    math.floor(len(my_list)/2)


def two_sum(my_list, my_target):
    for index, value in enumerate(my_list):
        for index_2, value_2 in enumerate(my_list):
            if index is not index_2:
                if my_target == (value + value_2):
                    return [index, index_2]


list1 = [-1, -2, -3, -4, -5]
target1 = -8
print(two_sum(list1, target1))
