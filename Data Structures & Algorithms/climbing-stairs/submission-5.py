class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n
        res=3
        prev=2
        for _ in range(3,n):
            tmp=res
            res=res+prev
            prev=tmp
        return res