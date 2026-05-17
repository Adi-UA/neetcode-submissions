class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if no prices
        if len(prices)<=1:
            return 0
        # check if price continuously increases
        for i in range(len(prices)-1):
            is_cts = True
            if prices[i+1]-prices[i] < 0:
                is_cts=False
                break
        if is_cts:
            return prices[len(prices)-1] - prices[0]
        # check if price continuously dropping
        for i in range(len(prices)-1):
            is_cts = True
            if prices[i+1]-prices[i] > 0:
                is_cts=False
                break
        if is_cts:
            return 0
        # all the same
        if max(prices)==min(prices):
            return 0
        # discontinuous case
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                max_profit = max(prices[j]-prices[i],max_profit)
        return max_profit

        