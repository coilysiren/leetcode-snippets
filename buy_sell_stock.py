# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i, buyPrice in enumerate(prices):
            for sellPrice in prices[i + 1 :]:
                maxProfit = max(maxProfit, sellPrice - buyPrice)

        return maxProfit
