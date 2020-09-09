from typing import List

## 使用dict查找表
## 时间复杂度：O(n)
def isAnagram(s: str, t: str) -> bool:
    dict1 = {}
    dict2 = {}
    if len(s) != len(t):
        return False
    for x in s:
        dict1[x] = dict1.get(x,0) + 1
    for x in t:
        dict2[x] = dict2.get(x,0) + 1
    for x in s:
        if dict1[x] != dict2.get(x):
            return False
    return True
