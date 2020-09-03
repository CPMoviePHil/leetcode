def move_zeroes(nums):
    index = 0
    counter = 0
    while counter < len(nums):
        if nums[index] == 0:
            k = nums.pop(index)
            nums.append(k)
        else:
            index += 1
        counter += 1
    return nums


arr = [0,1,0,3,12]
print(move_zeroes(arr))