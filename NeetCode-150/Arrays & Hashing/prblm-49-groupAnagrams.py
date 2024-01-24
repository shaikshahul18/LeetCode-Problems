from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)
    for string in strs:
        count = [0] * 26  # we are counting each letter in a given string
        for char in string:
            count[ord(char) - ord("a")] += 1
        res[tuple(count)].append(string)

    return res.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
