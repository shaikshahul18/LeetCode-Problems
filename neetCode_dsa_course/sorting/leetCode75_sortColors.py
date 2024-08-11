def sortColors(nums):
    l, r = 0, len(nums) - 1
    index = 0 
    
    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while index <= r:
        if nums[index] == 0:
            swap(l, index)
            l += 1
        elif nums[index] == 2:
            swap(index, r)
            r -= 1
            index -= 1
        index += 1
    return nums

print(sortColors([2,0,2,1,1,0]))