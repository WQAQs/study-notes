from typing import List

## 1.sort+hash map
## Time Complexity: O(n*klogk) where k is the max length of string in strs
## Space Complexity: O(n*k)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    str_dict = {}
    res = []
    for s in strs:
        key = "".join(sorted(s)) ## 因为sorted(s)返回的是一个list，要组装成一个string
        if str_dict.get(key) != None:
            str_dict[key].append(s)
        else:
            str_dict[key] = [s]
    for key in str_dict:
        res.append(str_dict[key])
    return res

strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(strs)
res


