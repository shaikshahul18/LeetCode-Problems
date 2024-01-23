def majorityElem(nums):
    # this code uses the moore's voting algorithm
    # ALWAYS KEEP IN MIND, THIS ALGO ONLY WORKS IF THE ELEMENT OCCURS MORE THAN 50%
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
