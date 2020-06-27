## 遍历整个股票交易日价格列表 price，
# 策略是所有上涨交易日都买卖（赚到所有利润）
# 所有下降交易日都不买卖（永不亏钱）。
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit