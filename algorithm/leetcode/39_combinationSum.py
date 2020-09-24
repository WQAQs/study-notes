'''
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
'''


class Solution(object):
    ### 背包问题（可重复使用0-1背包）
    # 与零钱兑换问题相似
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = {i: [] for i in range(target + 1)}
        dp[0] = [[]]
        for c in candidates:
            for num in range(c, target + 1):
                if dp[num - c]:
                    for a in dp[num - c]:
                        dp[num].append(a + [c])
        return dp[target]

    

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = {i : [] for i in range(target + 1)}
        dp[0] = [[]]
        for num in candidates:
            for data in range(num, target + 1):
                if dp[data - num]:
                    for a in dp[data - num]:
                        dp[data].append([num] + a)
        return dp[target]


