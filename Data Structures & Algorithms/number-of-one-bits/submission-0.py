class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n != 0:
            if n & 1: # check against 1's place
                count+=1
            n=n>>1
        return count