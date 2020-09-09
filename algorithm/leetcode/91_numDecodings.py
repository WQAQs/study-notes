def numDecodings(self, s: str) -> int:
    if len(s) <= 1:
        return len(s)
    # dp[i]中保存s[0,....,i]的解码方法数
    dp = [-1 for i in range(len(s))]
    dp[0] = 1
    dp[1] = 2 if (s[0] == '1' or (s[0] == '2'  and '6' - s[1] <= 0)) else 1
    for i in range(2, len(s)):
        temp = dp[i - 2] if  (s[i-1] == '1' or (s[i-1] == '2'  and '6' - s[i] <= 0))  else 0
        dp[i] = dp[i - 1] + temp
    return dp[-1]

