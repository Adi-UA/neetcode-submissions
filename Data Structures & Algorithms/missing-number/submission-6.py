class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums) # since i only 0->n-1 need to add n value artifically here
        for i in range(len(nums)):
            res+= i-nums[i]
        return res