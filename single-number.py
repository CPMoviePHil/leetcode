def single_number_arrays(nums):

    count = {}
    for i, v in enumerate(nums):
        if v in count.keys():
            count[v] += 1
        else:
            count[v] = 1
    return list(count.keys())[list(count.values()).index(1)]

def single_number_arrays_two(nums):

    n_d_list = []
    for v in nums:
        if v not in n_d_list:
           n_d_list.append(v)
        else:
            n_d_list.remove(v)
    return n_d_list[0]

print(single_number_arrays([1, 2, 2, 3, 4, 4, 4, 3]))
print(single_number_arrays_two([1, 2, 2, 3, 4, 4, 4, 3]))