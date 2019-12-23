def search(my_list, target):
    i = 0
    while i < len(my_list)//2:
        if target == my_list[i]:
            return my_list[i]
        i += 1
    print(my_list[round(len(my_list)/2):])
    # search(my_list[round(len(my_list)/2)-1:], target)


def two_sum(my_list, my_target):
    hash_dict = {}
    for index, value in enumerate(my_list):
        x = my_target - value
        if x not in hash_dict:
            hash_dict[value] = index
        else:
            return [hash_dict[x], index]


list1 = [2,7,11,15]
target1 = 9
# print(search(list1, target1))
print(two_sum(list1, target1))
