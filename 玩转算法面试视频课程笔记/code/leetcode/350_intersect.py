from typing import List

## 使用dict查找表
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    dict1 = {}
    dict2 = {}
    res = []
    for x in nums1:
        dict1[x] = dict1.get(x,0) + 1
    for x in nums2:
        dict2[x] = dict2.get(x,0) + 1
        temp = dict1.get(x,0)
        if temp > 0:
            res.append(x)
            dict1[x] = temp - 1
            dict2[x] = dict2.get(x,0) - 1
    return res
