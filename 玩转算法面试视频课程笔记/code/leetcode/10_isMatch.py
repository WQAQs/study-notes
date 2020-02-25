class Solution(object):
    def isMatch(self, s, p):
        """
        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        s 可能为空，且只包含从 a-z 的小写字母。
        p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

        输入:
            s = "ab"
            p = ".*"
        输出: true

        :type s: str
        :type p: str
        :rtype: bool
        """

        '''
        思考1：如果只有 . 没有 * 就比较简单，只需要从左到右检查匹配串s是否能匹配模式串p的每一个字符
        （1） 使用循环的方法
        '''
        def simple_match1(s, p):
            if len(s)!=len(p):
                return False
            for i in range(len(s)):
                c1 = s[i]
                c2 = p[i]
                if c1 != c2 and c2 != '.':
                    return False
            return True

        '''
        （2） 使用递归的方法
        '''
        def simple_match2(s, p):
            if not s or not p:
                return not s and not p
            first_match = p[0] in {s[0], '.'}
            return first_match and simple_match2(s[1:], p[1:])
        '''
        思考2：如果有 * 就麻烦了，需要检查匹配串的s的不同后缀，看它是否能够匹配模式串p剩余的部分 
        （1）使用回溯法   
        一旦递归层数过多 ！！！非常耗时！！！耗时指数倍增！！！
        
        attention: 
                    a. 递归就是刨根问底，一直往深层调用，直到达到终止条件才返回
                    b. 递归的返回是一层一层的返回
                    c. 举例说明：从最底层返回最底层的上一层递归点，然后再继续运行该递归点之后的程序,
                                直到该层可以返回，再向上返回，
                                ...
                                直到最初的调用层返回结果
        编程总结：
                思考的顺序：
                        a. 当前层要做什么处理？
                        b. 当前层需要下一层的什么结果，直接丢给下一层，不管下一层怎么运行，当前层只管用这个结果就行了
                        c. 递归终止条件！！
                code的顺序：
                        c. 递归终止条件！！
                        a. 当前层要做什么处理？
                        b. 当前层需要下一层的什么结果，直接丢给下一层，不管下一层怎么运行，当前层只管用这个结果就行了
                    
        '''
        def my_isMatch1(s, p):
            if not p:
                return not s

            first_match = bool(s) and p[0] in {s[0], '.'}

            if len(p) >= 2 and p[1] == '*':
                res1 = self.isMatch(s, p[2:])
                res2 = first_match and self.isMatch(s[1:], p)
                return (res1 or res2)
            else:
                return first_match and self.isMatch(s[1:], p[1:])

        def my_isMatch2(s, p):
            memo = {}

            def dp(i, j):
                if (i, j) not in memo:
                    if j == len(p):
                        ans = i == len(s)
                    else:
                        first_match = i < len(s) and p[j] in {s[i], '.'}
                        if j + 1 < len(p) and p[j + 1] == '*':
                            ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                        else:
                            ans = first_match and dp(i + 1, j + 1)

                    memo[i, j] = ans
                return memo[i, j]

            return dp(0, 0)
        '''
        memo: <class 'dict'>: 
        {
        (0, 4): False, 
        (1, 4): False, 
        (3, 5): True, 
        (2, 4): True, 
        (2, 2): True, 
        (1, 2): True, 
        (0, 2): True, 
        (0, 0): True
        }
        '''
#
        out = my_isMatch2(s, p)
        return out


so = Solution()
out = so.isMatch("aab", "c*a*b")
out
