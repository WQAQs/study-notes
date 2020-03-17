'''
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，
返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

'''
## 1.滑动窗口[l,r]
from typing import List
class Solution:
    @classmethod
    def findAnagrams(cls, s: str, p: str) -> List[int]:
        def check_same(freq_s,freq_p):
            for i in range(26):
                if freq_p != freq_s:
                    return False
            return True
        res = []
        l = 0
        r = -1
        freq_s=[0 for i in range(26)]
        freq_p=[0 for i in range(26)]
        for i in range(len(p)):
            freq_p[ord(p[i])-ord('a')] += 1
        while r + 1 < len(s) and len(p) > 0:
            r += 1
            freq_s[ord(s[r]) - ord('a')] += 1
            if r - l + 1 > len(p):
                freq_s[ord(s[l])-ord('a')] -= 1
                l += 1
            if r - l + 1 == len(p) and check_same(freq_s,freq_p):
                res.append(l)
        return res

if __name__ == "__main__":
    res = Solution.findAnagrams("cbaebabacd","abc")
    res

