class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        l=r=0
        while l < len(prices):
            while r < len(prices) and prices[r] >= prices[l]:
                max_profit = max(max_profit,prices[r]-prices[l])
                r+=1
            l=r
        return max_profit