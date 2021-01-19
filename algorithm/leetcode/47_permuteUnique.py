'''
47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    def permuteUnique(self, nums):
        res = []
        visit = [0 for i in range(len(nums))]
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return 
            for i in range(len(nums)):
                # 保证nums中重复的数，一定是按照从左向右的顺序填充path中的位置。
                # 要判断 i > 0 !!! 
                # 要使用逻辑取反： not
                temp = (i > 0 and nums[i] == nums[i - 1]) and (not visit[i - 1])
                if visit[i] or (i > 0 and (nums[i] == nums[i - 1]) and (not visit[i - 1])):
                    continue
                visit[i] = 1
                backtrack(path + [nums[i]])  # 自动包含了回溯后重置path的值，所以不用再另外重置path的值了
                visit[i] = 0
        nums.sort()
        backtrack([])
        return res

so = Solution()
res = so.permuteUnique([1,1,2])
