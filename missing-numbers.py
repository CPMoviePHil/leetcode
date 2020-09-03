def missing_number(nums):
    if nums[0] == 0 and len(nums) == 1:
        return 1
    biggest = max(nums)
    new_nums = list(range(biggest+2))
    for v in new_nums:
        if v not in nums:
            return v


def missing_numbers_2(nums):
    # [0,2,3,4]
    # list(range(len(nums)+1)) => [0, 1, 2, 3, 4]
    # 兩個總和相減一定會等於少掉的數字
    nums.sort()
    if nums[0] != 0:
        return 0
    return sum(list(range(len(nums)+1))) - sum(nums)


print(missing_number([3,0,1]))
print(missing_numbers_2([0,1]))