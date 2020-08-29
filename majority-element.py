def majority_element(nums):
    count = {}
    biggest = 0
    biggest_index = 0
    for i, v in enumerate(nums):
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
    for i, v in count.items():
        if biggest < v:
            biggest_index = i
            biggest = v
    return biggest_index

print(majority_element([2,2,1,1,1,2,2]))
