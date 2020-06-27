# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

# 示例:

# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    ## 1.动态规划
    ## dp[n]表示序列 1，2，...，n 的二叉搜索树个数
    ## 注意！！只要两个序列的个数相同，它们的二叉搜索树个数就相同，这就是重复子问题的来源
    ##        跟序列的具体值无关，只跟序列的个数有关，比如序列1，2和序列5，6的二叉搜索树个数相同
    ## f(i，n)表示以i为根的二叉搜索树的个数
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1]*dp[i - j]
        return dp[n]