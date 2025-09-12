class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l, r = 0, 1 # l -> buy. r -> sell
        maxProfit = 0

        while r < len(prices):
            # profitable?
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r

            r += 1

        return maxProfit