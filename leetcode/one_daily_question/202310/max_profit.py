import typing


class Solution:
    def maxProfit(self, prices: typing.List[int]) -> int:
        """
        max profit
        """
        is_have = False
        buy_price = 0
        profit = 0
        length = len(prices)
        for i, price in enumerate(prices):
            if i + 1 < length and price < prices[i + 1] and not is_have:
                buy_price = price
                is_have = True
            if i + 1 < length and price > prices[i + 1] and is_have:
                profit += (price - buy_price)
                is_have = False
        if is_have:
            profit += (prices[-1] - buy_price)
        return profit
    
    def maxProfit(self, prices: typing.List[int]) -> int:
        """
        max profit
        """
        # 定义二维数组，每个元素的0下标表示卖出的利润，1下标表示买入后的利润
        length = len(prices)
        dp = [[0, 0]] * length

        # 第一天只能不交易或者买入
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[length - 1][0]


if __name__ == '__main__':
    sol = Solution()
    prices = prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices=prices))
