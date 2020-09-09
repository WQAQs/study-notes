## 动态规划
def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0
    maxdp = 0
    predp = 0
    for i in range(1, len(prices)):
        dp = max(0, prices[i] - prices[i-1] + predp)
        predp = dp
        maxdp = max(maxdp, dp)
    return maxdp
    
## 滑动窗口
def maxProfit(self, prices: List[int]) -> int:
    minprice = int(1e9)
    res = 0
    for price in prices:
        res = max(res, price - minprice)
        minprice = min(minprice, price)
    return res
        