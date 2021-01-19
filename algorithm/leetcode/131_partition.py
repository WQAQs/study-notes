class Solution:
    # 回溯
    def partition(self, s):
        res = []
        def backtrack(path, s):
            if len(s) == 0:
                res.append(path)
                return
            for i in range(len(s)):
                segment = s[:(i + 1)]
                if is_huiwen(segment):
                    backtrack(path + [segment], s[(i + 1):])
                    ## 或者如下写法：
                    # backtrack(path.append(segment), s[(i + 1):])  
                    # path.pop()
        def is_huiwen(segment):
            left, right = 0, len(segment) - 1
            while left < right:
                if segment[left] != segment[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        backtrack([], s)
        return res

