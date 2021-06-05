class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        buy_idx = 0
        sell_idx = 0
        min_idx = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[min_idx]
            if profit < 0:
                min_idx = i
            elif profit > max:
                max = profit
                buy_idx = min_idx
                sell_idx = i
        return max
