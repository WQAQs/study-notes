class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        begin=0
        end=len(t)
        return True if self.dfs(s,t,begin,end) else False

    def dfs(self,s,t,begin,end):
        if len(s)==0:
            return True
        for i in range(begin,end):
            if s[0]==t[i]:
                if self.dfs(s[1:],t,i+1,end):
                    return 1
                return 0
so = Solution()
res = so.isSubsequence("abcd","wbk")
res
