class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def dfs(n):
            if n <=2:
                print(dp)
                dp[n]=n
                return dp[n]
            if dp[n]!=-1:
                return dp[n]
            # otherwise recurse
            dp[n]=dfs(n-1) + dfs(n-2)
            return dp[n]
        return dfs(n)