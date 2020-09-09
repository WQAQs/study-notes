from typing import List

## 1. 垂直扫描
## 时间复杂度：O(s)，s 为所有字符串的长度之和
## 空间复杂度：O（1）
def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    if len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != c:
                return res
        res += c
    return res

## 2. 水平扫描
## 时间复杂度：O(s)，s 为所有字符串的长度之和
## 空间复杂度：O（1）
def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    res = strs[0]
    for i in range(1, len(strs)):
        for j in range(len(res)):
            if j >= len(strs[i]) or res[j] != strs[i][j]:
                res = res[0:j]
                break
    return res

## 3. 分而治之
## 时间复杂度：
## 空间复杂度：
def longestCommonPrefix2(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    def solve(strs,start,end):
        if start == end:
            return strs[start]
        mid = start + (end - start)//2
        res1 = solve(strs, start, mid)
        res2 = solve(strs, mid + 1,end)
        i = 0
        while i < len(res1) and i < len(res2):
            if res1[i] != res2[i]:
                break
            i += 1
        return res1[0:i]
    return solve(strs,0,len(strs)-1)

strs = ["aa","a"]
res = longestCommonPrefix2(strs)
res
    


