class Solution:
    '''
    
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

    '''

    ## ##
    '''
    1. 分治方法 
    执行用时 :172 ms, 在所有 Python3 提交中击败了5.48%的用户
    内存消耗 :13.7 MB, 在所有 Python3 提交中击败了61.58%的用户
    '''
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return
        # 递归终止条件
        if n == 1:
            return nums[0]
        #### 分治 ####
        #### 划分子问题 ####
        max_l = self.maxSubArray(nums[0:n // 2])  # 计算左边的最大子序和
        max_r = self.maxSubArray(nums[n // 2:n])  # 计算右边的最大子序和
        # 计算中间的最大子序和
        l_max = nums[n//2 - 1]   # 计算左边部分的最大和
        temp = 0
        for i in range(n//2 - 1, -1, -1):
            temp += nums[i]
            l_max = max(l_max, temp)
        r_max = nums[n//2]  # 计算右边部分的最大和
        temp = 0
        for i in range(n//2, n):
            temp += nums[i]
            r_max = max(r_max, temp)
        #### 合并解决子问题 ####
        return max(l_max + r_max, max(max_l, max_r))  # 返回左边最大子序和，右边最大子序和，中间最大子序和 中最大的值

    '''
    2. 动态规划方法
    执行用时 :80 ms, 在所有 Python3 提交中击败了63.40%的用户
    内存消耗 :13.8 MB, 在所有 Python3 提交中击败了58.78%的用户
    
    时间复杂度：O(N), 只遍历一次数组。
    空间复杂度：O(1)，只使用了常数空间。
    '''
    def maxSubArray2(self, nums):
        n = len(nums)
        if n == 0:
            return
        max_res = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_res = max(nums[i], max_res)
        return max_res



nums = [-2,1,-3,4,-1,2,1,-5,4]
so = Solution()
out = so.maxSubArray(nums)
out