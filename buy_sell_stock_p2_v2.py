# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for a in range(len(prices) - 1):
            if prices[a] < prices[a + 1]:
                profit += prices[a + 1] - prices[a]

        return profit
