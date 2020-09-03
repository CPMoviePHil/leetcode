def contains_duplicate(nums):
    stack = {}
    for v in nums:
        if v not in stack.keys():
            stack[v] = 1
        else:
            return True
    return False

contains_duplicate([1,2,3,4])