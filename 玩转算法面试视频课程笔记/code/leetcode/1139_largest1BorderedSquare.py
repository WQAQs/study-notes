# 1139. 最大的以 1 为边界的正方形
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。

 

# 示例 1：

# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 示例 2：

# 输入：grid = [[1,1,0,0]]
# 输出：1
 

# 提示：

# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1

from typing import List

class Solution:
    ## 动态规划
    ## 使用三维数组dp[n][m][2]
    ## dp[i][j][0]表示grid[i][j]左边最长连续1的个数
    ## dp[i][j][1]表示grid[i][j]上边最长连续1的个数
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        dp = []
        res = 0
        for i in range(len(grid)+1):
            dp.append([[0]*2 for x in range(len(grid[0])+1)])
        for i in range(1, len(grid)+1):
            for j in range(1, len(grid[0])+1):
                if grid[i-1][j-1] == 1:
                    dp[i][j][0] += dp[i][j - 1][0] + 1
                    dp[i][j][1] += dp[i - 1][j][1] + 1
                    d = min( dp[i][j][0], dp[i][j][1])
                    while d > 0:
                        if dp[i - d + 1][j][0] >= d and dp[i][j - d + 1][1] >= d:
                            break
                        d -= 1
                    res = max(res, d)
        return res*res

so = Solution()
res = so.largest1BorderedSquare(grid=[[1,1,1],
                                      [1,0,1],
                                      [1,1,1]])
res

