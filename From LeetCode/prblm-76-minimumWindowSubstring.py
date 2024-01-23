def minWindow(s: str, t: str) -> str:
    m = len(s)
    n = len(t)
    for i in range(n, m):
        left = 0
        right = i
        while (left < right and right <= m):
            count = 0
            for string in t:
                print(string, s[left:right])
                if string in s[left:right]:
                    count += 1
            if count == n:
                return s[left:right]
            left += 1
            right += 1


print(minWindow("ADOBECODEBANC", "ABC"))
