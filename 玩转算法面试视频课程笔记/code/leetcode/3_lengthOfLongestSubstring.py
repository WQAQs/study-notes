'''
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

'''

## 使用滑动窗口nums[0,k]保存没有重复的字符
## 注意：python中字符转换为ASCII码要使用ord(),
## 不能用int(),int()只能将数字字符转换为对应的整数
def lengthOfLongestSubstring(s):
    l = 0
    r = -1 # s[l,r]范围内保存不重复子串
    freq = [0 for i in range(256)] # 保存字符在子串中出现的次数，索引为字符的scii值
    res = 0
    while l < len(s):
        if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
            r += 1
            freq[ord(s[r])] += 1
        else:
            freq[ord(s[l])] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
    

