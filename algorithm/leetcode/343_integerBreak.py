# 暴力解法 
# 时间复杂度：O（2^n）
def integerBreak(self, n: int) -> int:
    if n == 2:
        return 1
    res = -1
    for i in range(1, n):
        res = max(res, i*(n-i), i*self.integerBreak(n-i))
    return res

# 动态规划
def integerBreak(self, n: int) -> int:
    if n == 2:
        return 1
    dp = [-1 for i in range(n+1)]
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
    return dp[n]
