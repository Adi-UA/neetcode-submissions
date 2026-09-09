class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        minimum=nums[0]
        # move r to min of sorted and l to max+1 of sorted
        while l<r:
            mid=(l+r)//2
            if nums[mid] < nums[r]: # [5 2 3 4] i.e. L > M
                r=mid
            # if mid >= r [2 3 4 1] i.e. L < M
            else:
                l = mid+1
        return nums[l]