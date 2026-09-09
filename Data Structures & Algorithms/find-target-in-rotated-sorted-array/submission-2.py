class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m] < nums[r]:
                r=m
            else:
                l=m+1
        pivot=l
        if target in nums[0:pivot]:
            low,high=0,pivot
        else:
            low,high=pivot,len(nums)-1
        # binary search
        while low <= high:
            m=(low+high)//2
            if target==nums[m]:
                return m
            elif target < nums[m]:
                high=m-1
            else:
                low=m+1
        return -1
