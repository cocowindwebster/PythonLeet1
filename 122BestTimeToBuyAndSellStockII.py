class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #ERROR1:Input [1] Output : 1 Expected : 0
        if prices == None or len(prices)  == 0 :
            return 0
        previous = prices[0]
        sum = 0
        for current in prices[1:]:
            if current > previous:
                sum += current - previous
            previous = current
        return sum
