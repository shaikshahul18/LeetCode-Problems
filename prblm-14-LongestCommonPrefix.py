def longestCommonPrefix(List):
    if len(List) == 0:
        return ''
    prefix = List[0]
    for string in List[1:]:
        while prefix != string[0:len(prefix)]:
            prefix = prefix[0:len(prefix)-1]

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
