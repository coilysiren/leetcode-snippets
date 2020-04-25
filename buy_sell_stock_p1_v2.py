# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# time: O(n) - loops through the list once
# space: O(1) - only 2 values stored
#
# written b/c v1 is slow enough to timeout
# v1 => https://github.com/lynncyrin/leetcode-snippets/blob/master/buy_sell_stock_v1.py


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) < 2:
            return profit

        nextBuyPrice = prices[0]

        for price in prices:
            # check if we can move both the sell price and the buy price b/c new sell price
            if (price - nextBuyPrice) > (profit):
                print(f"sell price to {price}, buy price to {nextBuyPrice}")
                profit = price - nextBuyPrice

            # check if we should move the buy price b/c its lower
            elif price < nextBuyPrice:
                print(f"potential buy price to {price}")
                nextBuyPrice = price

        return profit
