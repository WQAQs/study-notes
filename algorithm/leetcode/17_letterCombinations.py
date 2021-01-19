'''17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''

class Solution:
    # 方法1: 使用迭代
    def letterCombinations1(self, digits):
        if len(digits) == 0:
            return ""
        output = [""]
        dic_phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                     '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        for s in digits:
            temp = []
            for res in output:
                for letter in dic_phone[s]:
                    temp.append(res + letter)
            output = temp

    # 方法2: 使用回溯
    def letterCombinations(self, digits):
        if not digits: return []
        res = []
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        def backtrack(combination, digits):
            if len(digits) == 0:
                res.append(combination)
            else:
                for a in phone[digits[0]]:
                    backtrack(combination + a, digits[1:])
        backtrack('',digits)
        return res

so = Solution()
out = so.letterCombinations2("23")
out

