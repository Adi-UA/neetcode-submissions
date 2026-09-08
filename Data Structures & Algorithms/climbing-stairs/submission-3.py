class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(curr, n):
            if curr > n:
                return 0
            elif curr == n:
                return 1
            if curr in memo:
                return memo[curr]
            memo[curr] = dfs(curr + 1, n) + dfs(curr + 2, n)
            return memo[curr]

        return dfs(0, n)