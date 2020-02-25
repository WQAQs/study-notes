class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            # 要考虑stack是不是为空，否则使用pop()函数会报错
            # 要考虑 char是不是在 dic 的key值中
            if char in dic and len(stack) > 0:
                top = stack.pop()
                if top != dic[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

so = Solution()
out = so.isValid("]")
out



