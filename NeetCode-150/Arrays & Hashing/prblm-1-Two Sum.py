def twoSum1(nums,target):
    # Brute Force
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

def twoSum2(nums,target):
    # This is using hash table, two pass
    numMap = {}
    n = len(nums)

    for i in range(n):
        numMap[nums[i]] = i
    
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    
    return []

def twoSum3(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []

print(twoSum3([3,3],6))


