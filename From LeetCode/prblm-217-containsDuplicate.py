def containDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(n):
        if nums[i] == nums[i+1]:
            return True
    return False


print(containDuplicate([1, 2, 3, 1]))
