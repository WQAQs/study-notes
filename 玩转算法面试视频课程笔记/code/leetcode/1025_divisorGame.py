import math

class Solution:
    def divisorGame(self, N: int) -> bool:
        ## trick:奇数的因数只能是奇数，所以如果某个玩家占到奇数，那么她选择的因数就是一个奇数，则丢给对方玩家的就是偶数了
        ##       偶数的因数可以是奇数也可以是偶数，只要占到偶数的玩家选择的是奇数因子，那么丢给对方的始终为奇数，
        ##       然后自己再得到的始终为偶数，考虑最终的占到2的赢，占到1的输。
        ## 所以只用判断爱丽丝能不能一开始拿到偶数，能拿到偶数，那么按照上面的策略，她一定会赢。
        return N%2 == 0
    ## 2.动态规划
    ## dp[i]表示占到数字i的玩家的输赢结果。
    ## 由于一开始的数字是N，并且是爱丽丝开始的第一轮。
    ## 题目要求爱丽丝最终的输赢，即要求dp[N]
    def divisorGame(self, N: int) -> bool:
        dp = [0 for i in range(N+1)]
        dp[1] = 0 #若爱丽丝抽到1，则爱丽丝输
        if N<=1:
            return False
        else:
            dp[2] = 1 #若爱丽丝抽到2，则爱丽丝赢
            for i in range(3,N+1):
                for j in range(1,i):
                    # 若j是i的约数, 且dp[i-j]==0 即意味着爱丽丝
                    if i%j==0 and dp[i-j]==0:
                        dp[i] = 1
                        break
            return dp[N]==1

so = Solution()
# res = so.divisorGame(24)
res = so.lisrtFactor(24)