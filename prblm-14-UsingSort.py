def longestCommonPrefix(List):
    sorted(List)
    first = List[0]
    last = List[-1]
    prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return prefix
        prefix += first[i]
    return prefix


print(longestCommonPrefix(["flow", "flower", "flight"]))
