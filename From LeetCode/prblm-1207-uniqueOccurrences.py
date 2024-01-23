def uniqueOccurrences(arr):
    hashMap = {}
    for i in arr:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1

    values = set(hashMap.values())
    return len(values) == len(hashMap.values())


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
