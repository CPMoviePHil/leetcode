
def search_insert(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        index = 0
        for i, v in enumerate(arr):
            if target > v:
                index = i + 1
        return index


print(search_insert([1,3,5,6], 2))
