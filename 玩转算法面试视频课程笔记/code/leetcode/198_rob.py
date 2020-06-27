## 动态规划
### 状态dp[i]的定义是：在[0,...,i]这个范围内打家劫舍的最大金额，
### 注意！并没有指定要偷nums[i]这一家啊！
### 这里因为在求dp[i]的时候只用到了前两项：dp[i-1]和dp[i-2]，
### 所以用的是三个变量dp1, dp2 , dp，而没有用dp数组
def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    dp1, dp2 , dp = nums[0], max(nums[0], nums[1]), -1 
    for i in range(2,len(nums)):
        dp = max(dp1 + nums[i], dp2)
        dp1, dp2 = dp2, dp
    return dp

def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    # 子问题：
    # f(k) = 偷 [0..k) 房间中的最大金额

    # f(0) = 0
    # f(1) = nums[0]
    # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }

    N = len(nums)
    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = nums[0]
    for k in range(2, N+1):
        dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
    return dp[N]
