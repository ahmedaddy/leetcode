class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = float("inf")
        profit = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit = max(profit, price - buy1)
        return profit
