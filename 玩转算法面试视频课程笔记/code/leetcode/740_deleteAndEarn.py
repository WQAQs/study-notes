# 740. 删除与获得点数
# 给定一个整数数组 nums ，你可以对它进行一些操作。

# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

# 示例 1:

# 输入: nums = [3, 4, 2]
# 输出: 6
# 解释: 
# 删除 4 来获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 来获得 2 个点数。总共获得 6 个点数。
# 示例 2:

# 输入: nums = [2, 2, 3, 3, 3, 4]
# 输出: 9
# 解释: 
# 删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
# 注意:

# nums的长度最大为20000。
# 每个整数nums[i]的大小都在[1, 10000]范围内。

class Solution:
    # 动态规划
    ## 转换成打家劫舍的问题
    ## 定义一个新数组all[],all数组中的索引是nums数组中的元素值，
    ## all中索引i位置上的值是数字i在nums数组中出现的次数
    ## dp[i]即为对于all数组[0，1，...，i]范围内能得到的最大点数,
    ## dp[i] = max(dp[i-1],dp[i-2]+all[i]*i)
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums_max = nums[0]
        # 构建all数组
        for x in nums:
            nums_max = max(nums_max, x)
        all = [0] * (nums_max + 1)
        for x in nums:
            all[x] += 1
        # dp状态转移 
        dp = [0] * (nums_max + 1)
        dp[1] = all[1] * 1
        for i in range(2, nums_max + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + all[i] * i)
        return dp[nums_max]