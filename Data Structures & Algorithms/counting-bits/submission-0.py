class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(num):
            count=0
            while num != 0:
                if num & 1: # check against 1's place
                    count+=1
                num=num>>1
            return count
        res=[]
        for i in range(n+1):
            res.append(helper(i))
        return res