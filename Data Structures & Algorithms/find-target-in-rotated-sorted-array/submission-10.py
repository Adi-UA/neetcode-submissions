class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min/max
        # decide which half to search in
        # binary search
        l,r=0,len(nums)-1
        while l<r:
            m=int((l+r)//2)
            if nums[m]<=nums[r]:
                r=m
            else:
                l=m+1
        if target in nums[l:]:
            r=len(nums)-1
        else:
            l,r=0,l
        while l<r:
            m=int((l+r)//2)
            print(l,r,nums[m])
            if nums[m]<target:
                l=m+1
            else:
                r=m
        return l if nums[l]==target else -1