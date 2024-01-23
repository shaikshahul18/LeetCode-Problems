def findContentChild(g, s):
    numCookies = len(s)
    if numCookies == 0:
        return 0

    g.sort()
    s.sort()

    maxNum = 0
    cookieIndex = numCookies - 1
    childIndex = len(g) - 1
    while cookieIndex >= 0 and childIndex >= 0:
        if s[cookieIndex] >= g[childIndex]:
            maxNum += 1
            cookieIndex -= 1
            childIndex -= 1
        else:
            childIndex -= 1
    return maxNum

def findContentChild(g, s):
    numCookies = len(s)
    if numCookies == 0:
        return 0

    g.sort()
    s.sort()
    gIndex = 0
    sIndex = 0
    maxNum = 0
    while(gIndex < len(g) and sIndex < len(s)):
        if g[gIndex] <= s[sIndex]:
            maxNum += 1
            gIndex += 1
            sIndex += 1
        else:
            sIndex += 1
    return maxNum