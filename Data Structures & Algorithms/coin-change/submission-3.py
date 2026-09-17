class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("infinity")]* (amount+1)
        dp[0]=0
        # add all dp[1] to dp[amount] values
        for amt in range(1,amount+1):
            for c in coins:
                if amt-c>=0:
                    # this builds up when dp[a-c] is 0 or exists already
                    dp[amt]=min(dp[amt],1+dp[amt-c]) 
        return dp[amount] if dp[amount]<=amount else -1