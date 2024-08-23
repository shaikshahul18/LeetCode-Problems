def guessNumber(n):
    low = 1
    high = n
    while (low <= high):
        mid = (low+high) // 2
        if guess(mid) < 0:
            high = mid - 1
        elif guess(mid) > 0:
            low = mid + 1
        else:
            return mid
    
def guess(n):
    if n > 6:
        return -1
    elif n < 6:
        return 1
    else:
        return 0
    

print(guessNumber(10))
