class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        minBuy = prices[0]
        maxProf = -1
        while i < len(prices):
            prof = prices[i] - minBuy
            maxProf = max(prof, maxProf)

            minBuy = min(prices[i], minBuy)
            i += 1
        
        if maxProf <= 0:
            return 0
        else:
            return maxProf
        