from typing import List
'''
290. 单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
'''
## 一定要注意！！正反都是唯一的映射关系，所以要使用两个映射表
## 时间复杂度：O(n)
## 空间复杂度：O(n)
def wordPattern(pattern: str, str: str) -> bool:
    mystr = str.split()
    dict1 = {}
    dict2 = {}
    if len(mystr) != len(pattern):
        return False
    else:
        for i in range(len(pattern)):
            if  not(pattern[i] in dict1) and not(mystr[i] in dict2):
                dict1[pattern[i]] = mystr[i]
                dict2[mystr[i]] = pattern[i]
            elif dict1.get(pattern[i]) != mystr[i] or dict2.get(mystr[i]) != pattern[i]:
                return False
        return True
    
pattern = "aaaa"
str = "dog og dog dog"
res = wordPattern(pattern, str)
res

