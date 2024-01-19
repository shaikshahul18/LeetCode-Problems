def removeElement(nums, val):
    n = len(nums)
    index = 0
    for i in range(n):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


print(removeElement([3, 2, 3, 2, 2], 3))
