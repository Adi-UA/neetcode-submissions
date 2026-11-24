class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        # search by finding min
        while l < r:
            m=int((l+r)//2)
            if nums[l]<nums[r]:
                return nums[l]
            elif nums[m]>nums[r]:
                l=m+1
            elif nums[m]<nums[r]:
                r=m
        return nums[l]