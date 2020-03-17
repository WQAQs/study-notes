from typing import List

## 使用set查找表
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    res = []
    for x in set1:
        if x in set2:
            res.append(x)
    return res