class Solution:
    def rob(self, nums: List[int]) -> int:
        curr,prev=nums[0],0
        for i in range(1,len(nums)):
            tmp=curr
            curr=max(curr,prev+nums[i])
            print(i,curr)
            prev=tmp
        return curr
        