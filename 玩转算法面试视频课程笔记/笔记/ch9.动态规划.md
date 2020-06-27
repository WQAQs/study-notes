# 动态规划
## 1. 基本概念
**记忆化搜索**——自上而下解决问题（递归）+ 用数组存储计算结果，避免了重复计算
            函数调用占用栈空间，对memory数组访问次数比动态规划多
**动态规划**——自下而上解决问题，用数组存储计算结果，避免了重复计算
    定义：将原问题拆分成若干个子问题，同时保存子问题的答案，使得每个子问题只求解一次，最终获得原问题的答案。

<img src = '..\\images\\ch9_dp.png'>

对于最优化问题：
<img src = '..\\images\\ch9_dp3.png'>

思考的过程：通常是先自顶向下思考解题思路，然后试图转换成自底向下的方法来优化。
**例题**：
 斐波拉契数


## 2. 第一个动态规划问题
**例题**：
70.Climbing Stairs  
```python
# 使用迭代
def climbStairs(self, n: int) -> int:
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2] 
    return dp[n]

def climbStairs(self, n: int) -> int:
    first, second = 1, 2
    for i in range(2,n):  # 从第三个阶梯开始
        res = first + second
        first = second
        second = res 
    return res
```

<img src ='..\\images\\ch9_dp2.png'>
120.Triangle 
```python
# 自底向上动态规划
def minimumTotal(self, triangle: List[List[int]]) -> int:
    n = len(triangle)
    for row in range(n-2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] = min(triangle[row+1][col] + triangle[row][col], triangle[row+1][col+1] + triangle[row][col])
    return triangle[0][0]
```
64.Minimum Path Sum
```python
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
```

## 3. 第3节
**例题**
**1. 一个练习题**
**整数拆分的可能分法**
将正整数n拆分成k份（使k个数之和的等于n）,且每种拆分方案不能为空，任意两种拆分方案不能相同（不考虑顺序）。例如：n＝7，k＝3，共4种拆分方法为：①1、1、5； ②1、2、4； ③1、3、3； ④2、2、3。下面三种分法被认为是相同的：1、1、5； 1、5、1；  5、1、1；

编程任务：

    给定的正整数n，分成k分，编程计算有多少种不同的分法。

数据输入：

    输入数据只有一行2个数：n、k (6<n≤200，   2≤k≤6)。

结果输出:

    输出数据是一个，有多少种不同的分法。

输入输出样例：

    输入：  7  3

    输出：  4   

（1）暴力解法：
时间复杂度O（n^k）
```C++
#include "stdio.h"
#include "stdlib.h"

int count;

void Select(int step,int cur,int n,int k,int sum)
{
    int i;

    if(sum>n) return;

    if(step>k)
    {
        if(n==sum)
        count++;
        return;
    }
    for(i=cur;i<=n;i++)
    {
        Select(step+1,i,n,k,sum+i);
    }
}

int main()
{
    int n,k;
    while(scanf("%d%d",&n,&k)!=EOF)
    {
        count=0;
        Select(1,1,n,k,0);
        printf("%d\n",count);
    }
    return 0;
}
```

343 
暴力解法：回溯遍历将一个数做分割的可能性O（2^n）
```python
# 暴力解法 
# 时间复杂度：O（2^n）
def integerBreak(self, n: int) -> int:
    if n == 2:
        return 1
    res = -1
    for i in range(1, n):
        res = max(res, i*(n-i), i*self.integerBreak(n-i))
    return res

# 动态规划
def integerBreak(self, n: int) -> int:
    if n == 2:
        return 1
    dp = [-1 for i in range(n+1)]
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
    return dp[n]

```

279
91
62
63

## 4.
198 
对状态的定义：
（1）考虑偷取[x,...,n-1]范围里的房子（函数定义）
（2）考虑偷取[0,...,x]范围里的房子（函数定义） 
213 
337
309 

## 5.
0-1背包问题  ：需要两个参数来定义状态！
空间复杂度的优化1
空间复杂度的优化2

0-1背包问题更多的变种：
    多重背包：每个物品不止一个，有num(i)个
    完全背包：每个物品可以无限使用
    多维费用背包问题：
    物品间加入更多约束（排斥，依赖） 

## 6.
300. 最长上升子序列
376. wiggle subsequence
最长公共子序列
 