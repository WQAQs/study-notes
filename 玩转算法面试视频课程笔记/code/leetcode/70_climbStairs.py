# 使用迭代
def climbStairs(self, n: int) -> int:
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2] 
    return dp[n]

def climbStairs(self, n: int) -> int:
    first, second = 1, 2
    for i in range(2,n):  # 从第三个阶梯开始
        res = first + second
        first = second
        second = res 
    return res