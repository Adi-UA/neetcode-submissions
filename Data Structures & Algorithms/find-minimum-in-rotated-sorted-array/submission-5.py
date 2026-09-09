class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minimum=nums[0]
        while l<r:
            mid=(l+r)//2
            if nums[l] < nums[r]:
                minimum=nums[l]
                l=r
            # left side is sorted, m is max of sorted
            elif nums[l]<=nums[mid]:
                minimum=nums[mid+1]
                l=mid+1
            # right side is sorted m is min of sorted
            else:
                minimum=nums[mid]
                r=mid
        return minimum