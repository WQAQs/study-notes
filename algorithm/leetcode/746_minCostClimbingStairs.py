class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp1, dp2 = 0, 0
        dp = 0
        for i in range(2, len(cost) + 1):
            dp = min(dp1 + cost[i-2], dp2 + cost[i-1])
            dp1, dp2 = dp2, dp
        return dp


