class Solution:
    def climbStairs(self, n: int) -> int:
        res=1
        prev=1
        for _ in range(n-1):
            tmp=res
            res=res+prev
            prev=tmp
        return res