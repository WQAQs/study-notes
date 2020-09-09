'''76. 最小覆盖子串
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''
import time
from collections import Counter
class Solution:
    ##1.使用滑动窗口[l,r]
    def minWindow(self, s: str, t: str) -> str:
        def check_in(freq_s,freq_t):
            for i in range(256):
                if freq_t[i] != 0 and freq_t[i] > freq_s[i]:
                    return False
            return True
        l = 0
        r = -1
        freq_s = [0 for i in range(256)]
        freq_t = [0 for i in range(256)]
        res_len = len(s) + 1
        res_l = -1
        for char in t:
            freq_t[ord(char)] += 1
        while l < len(s):
            if r + 1 < len(s) and not check_in(freq_s,freq_t): # 没找到并且没找到底，继续往后找(r += 1)
                r += 1
                freq_s[ord(s[r])] += 1
            else:  # 找到底了，或者找到满足的子串了
                freq_s[ord(s[l])] -= 1      
                l += 1
            if r - l + 1 >= len(t) and check_in(freq_s,freq_t):  # 找到了一个满足题意的子串
                if r - l + 1 < res_len:  # 更新res_len
                    res_l = l
                    res_len = r - l + 1
        if res_len == len(s) + 1:
            return ""
        return s[res_l:res_l+res_len]

    def minWindow1(self, s: str, t: str) -> str:
            if not t or not s:
                return ""
            # Dictionary which keeps a count of all the unique characters in t.
            dict_t = Counter(t)
            # Number of unique characters in t, which need to be present in the desired window.
            required = len(dict_t)
            l, r = 0, 0
            # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
            # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
            formed = 0
            # Dictionary which keeps a count of all the unique characters in the current window.
            window_counts = {}
            # ans tuple of the form (window length, left, right)
            ans = float("inf"), None, None
            while r < len(s):
                # Add one character from the right to the window
                character = s[r]
                window_counts[character] = window_counts.get(character, 0) + 1
                # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
                if character in dict_t and window_counts[character] == dict_t[character]:
                    formed += 1
                # Try and co***act the window till the point where it ceases to be 'desirable'.
                while l <= r and formed == required:
                    character = s[l]
                    # Save the smallest window until now.
                    if r - l + 1 < ans[0]:
                        ans = (r - l + 1, l, r)
                    # The character at the position pointed by the `left` pointer is no longer a part of the window.
                    window_counts[character] -= 1
                    if character in dict_t and window_counts[character] < dict_t[character]:
                        formed -= 1
                    # Move the left pointer ahead, this would help to look for a new window.
                    l += 1    
                # Keep expanding the window once we are done co***acting.
                r += 1    
            return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

if __name__ == "__main__":
    so = Solution()
    #### 验证了Counter()函数的时间复杂度是O(n)
    t = "qwertyuiopasdfghjkl;zxcvbnm,./qwertyuiopasdfghjkl;zxcvbnm,./qwertyuiopasdfghjkl;zxcvbnm,./qwertyuiopasdfghjkl;zxcvbnm,./qwertyuiopasdfghjkl;zxcvbnm,./"
    t1 = ""
    t2 = ""
    for i in range(10000):
        t1 = t1 + t
    for i in range(40000):
        t2 = t2 + t
    t0 = time.clock()
    dict_t = Counter(t1)
    print(time.clock() - t0)
    t0 = time.clock()
    # res = so.minWindow1("bbacacbbaacbbaacxbbcaawcdscsbbaacbbaacbfbaacbbaafcbbaacbbahacbbaacbbaacbbaacbbaacbbaacbbaacbbacacbbaacbbaacxbbcaawcdscsbbaacbbaacbfbaacbbaafcbbaacbbahacbbaacbbaacbbaacbbaacbbaacbbaac","rweddoyrxxgsa")
    dict_t = Counter(t2)
    print(time.clock() - t0)

    res = so.minWindow1("bbacacbbaacbbaacxbbcaawcdscsbbaacbbaacbfbaacbbaafcbbaacbbahacbbaacbbaacbbaacbbaacbbaacbbaacbbacacbbaacbbaacxbbcaawcdscsbbaacbbaacbfbaacbbaafcbbaacbbahacbbaacbbaacbbaacbbaacbbaacbbaac","rweddoyrxxgsa")
    res

            




