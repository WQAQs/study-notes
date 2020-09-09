class Solution:

    '''

    17. 电话号码的字母组合
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    示例:
    输入："23"
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

    '''

    # 方法1 使用迭代
    def letterCombinations1(self, digits: str):
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

    # 方法2 使用递归
    def letterCombinations2(self, digits):
        out = []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def myiter(res, digits):
            if not digits:
                out.append(res)
                return
            temp = digits[0]
            for char in dic[temp]:
                myiter(res + char, digits[1:])

        # if len(digits) == 0:
        if not digits:
            return ""
        myiter("", digits)
        return out

so = Solution()
out = so.letterCombinations2("23")
out

