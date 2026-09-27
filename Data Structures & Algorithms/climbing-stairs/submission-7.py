class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        def dfs(n):
            if n <=2:
                print(dp)
                dp[n]=n
            if dp[n]!=0:
                return dp[n]
            # otherwise recurse
            count=0
            for i in range(1,3):
                print(n-i)
                count+=dfs(n-i) if n-i>0 else 0
            dp[n]=count
            return dp[n]
        return dfs(n)