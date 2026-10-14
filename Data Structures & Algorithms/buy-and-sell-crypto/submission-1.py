class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 
        worst = prices[0]
        for sell in prices: 
            best = max(best, sell - worst)
            worst = min(worst, sell)
        return best 