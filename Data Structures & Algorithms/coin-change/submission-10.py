class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        # base case:
        dp[0]=0
        # check
        for i in range(1,amount+1):
            for j in range(len(coins)):
                target=i-coins[j]
                if target < 0:
                    continue
                if dp[target] != -1:
                    if dp[i]==-1:
                        dp[i]=1+dp[target]
                    else:
                        dp[i]=min(dp[i],1+dp[target])
        return dp[amount]