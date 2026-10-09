class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("infinity")]*(amount+1)
        # base case:
        dp[0]=0
        # check
        for amt in range(1,amount+1):
            for c in coins:
                if amt-c >=0:
                    dp[amt]=min(dp[amt],1+dp[amt-c])
        return dp[amount] if dp[amount] != float("infinity") else -1