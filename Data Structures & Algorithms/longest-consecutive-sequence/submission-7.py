class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        res=1
        longest=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                longest+=1
            elif nums[i]-nums[i-1]==0:
                continue
            else:
                longest=1
            res=max(longest,res)
        return res
