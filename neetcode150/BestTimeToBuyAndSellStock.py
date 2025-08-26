class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        low = prices[0]
        i = 1
        while i < len(prices):
            if prices[i] <= low:
                low = prices[i]
            else:
                profit = max(profit, prices[i] - low)
            i += 1

        return profit
