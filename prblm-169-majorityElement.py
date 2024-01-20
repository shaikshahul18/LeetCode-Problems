def majorityElement(nums):
    nums.sort()
    n = len(nums)
    return nums[n//2]
