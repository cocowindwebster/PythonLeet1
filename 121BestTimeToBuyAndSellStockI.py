class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0
        max_profit = 0
        min_prices = prices[0]
        for each in prices:
            min_prices = min(each, min_prices)
            max_profit = max(each - min_prices, max_profit)
        return max_profit