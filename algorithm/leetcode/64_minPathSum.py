from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    # dp = grid[0]    ！！！！！！这个地方有个深坑！！！更改了dp的时候，同时更改了grid，不能这样写！！！！
    dp = [0 for i in range(len(grid[0]))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == 0 and col == 0: dp[col] = grid[0][0]
            elif row == 0: dp[col] = dp[col-1] + grid[row][col] 
            elif col == 0: dp[col] = dp[col] + grid[row][col] 
            else : dp[col] = min(dp[col-1], dp[col])+grid[row][col] 
    return dp[-1]

res = minPathSum(grid=[[1,3,1],[1,5,1],[4,2,1]])