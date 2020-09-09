'''
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
'''

## 使用两个映射表表示正反唯一的映射关系，同290一样的解题思路
## 时间复杂度：O(n)
## 空间复杂度：O(n)
def isIsomorphic(self, s: str, t: str) -> bool:
    dict1 = {}
    dict2 = {}
    if len(t) != len(s):
        return False
    else:
        for i in range(len(s)):
            if  not(s[i] in dict1) and not(t[i] in dict2):
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
            elif dict1.get(s[i]) != t[i] or dict2.get(t[i]) != s[i]:
                return False
        return True