#1. valley, peak
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        valley = 0
        peak = 0
        while (i < len(prices) - 1):
            while (i < len(prices) - 1 and prices[i] >= prices[i + 1]):
                i += 1
            valley = prices[i]
            while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):  
                i += 1
            peak = prices[i]
            profit += peak - valley
        return profit    
        
#2. add continously, 只要后面比当前大就add         
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        while (i < len(prices) - 1):
            if (prices[i] < prices[i + 1]):
                profit += prices[i + 1] - prices[i]
            i += 1
        return profit  
