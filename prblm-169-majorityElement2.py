def majorityElem(nums):
    hashMap = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in hashMap:
            hashMap[nums[i]] += 1
        else:
            hashMap[nums[i]] = 1

    for key, value in hashMap.items():
        if value > n//2:
            return key
