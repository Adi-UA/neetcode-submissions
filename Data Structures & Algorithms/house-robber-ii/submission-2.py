class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def maxrob(l,u):
            lrob,rrob=0,0
            for n in nums[l:u]:
                tmp=lrob
                lrob=rrob
                rrob=max(n + tmp,lrob)
            return rrob
        return max(maxrob(0,len(nums)-1),maxrob(1,len(nums)))