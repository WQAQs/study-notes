from typing import List

## 1. hash map
## 时间复杂度：O(n^2)
## 空间复杂度：O(n^2)
def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    sum_dict = {}
    res = 0
    for c in C:
        for d in D:
            sum_dict[c + d] = sum_dict.get(c+d,0) + 1
    for a in A:
        for b in B:
            if sum_dict.get(0-a-b) != None:
                res += sum_dict[0-a-b]
    return res

## 2. 另一种使用hash map 的方式
## 时间复杂度：O(n^2)
## 空间复杂度：O(n^2)
def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    sum_dict1 = {}
    sum_dict2 = {}
    res = 0
    for a in A:
        for b in B:
            sum_dict1[a + b] = sum_dict1.get(a+b,0) + 1
    for c in C:
        for d in D:
            sum_dict2[c + d] = sum_dict2.get(c+d,0) + 1
    for two_sum in sum_dict1.keys():
        if sum_dict2.get(0-two_sum) != None:
            res += sum_dict1[two_sum]*sum_dict2[0-two_sum] 
    return res
    