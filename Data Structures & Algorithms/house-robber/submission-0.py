class Solution:
    def rob(self, nums: List[int]) -> int:
        lrob,rrob=0,0
        for n in nums:
            tmp=lrob
            lrob=rrob
            rrob=max(n + tmp,lrob)
        return rrob