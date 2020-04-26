# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# time: O(n^2) - loops through the list for every entry
# space: O(1) - only 1 value stored


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i, buyPrice in enumerate(prices):
            for sellPrice in prices[i + 1 :]:
                maxProfit = max(maxProfit, sellPrice - buyPrice)

        return maxProfit
