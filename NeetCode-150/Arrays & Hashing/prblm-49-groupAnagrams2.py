from collections import defaultdict


def groupAnagrams(strs):
    map = defaultdict(list)
    for string in strs:
        key = "".join(sorted(string))
        map[key].append(string)
    return list(map.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
