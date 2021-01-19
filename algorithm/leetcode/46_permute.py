'''46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums):
        res = []
        def backtrack(path, nums):
            if len(nums) == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                temp = nums[0]
                nums[0], nums[i] = nums[i], temp
                backtrack(path + [nums[0]], nums[1:])
                nums[i] = nums[0]
                nums[0] = temp
        backtrack([], nums)
        return res