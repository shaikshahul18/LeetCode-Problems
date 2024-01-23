def validAnagram(s, t):
    if len(s) != len(t):
        return False

    hashMap = {}
    for i in s:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1
    for i in t:
        if i in hashMap:
            hashMap[i] -= 1
            if hashMap[i] < 0:
                return False
        else:
            return False
    return True


print(validAnagram("anagram", "nagaram"))
