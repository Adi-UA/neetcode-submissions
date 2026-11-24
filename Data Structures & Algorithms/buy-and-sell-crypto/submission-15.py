class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        maximum=0
        l,r=0,1
        while l<r and r < len(prices):
            print(l,r)
            maximum=max(maximum,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l=r
            r+=1
        return maximum