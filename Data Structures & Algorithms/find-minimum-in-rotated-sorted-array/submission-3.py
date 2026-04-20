class Solution:
    def findMin(self, nums: List[int]) -> int:
        # during rotations l,r should start off the closest where r<l for all rotations
        # min val flanked by largest/smallest: move r to smallest val, l to highest val

        # start at ends
        l,r = 0, len(nums) - 1
        minVal = nums[r]
        # look at midpoint
        while l <= r:
            m = (l+r) // 2
            print(l,r,m)
            minVal = min(nums[m], minVal)
            # if l<m<r list is ascending and l is min
            if nums[l]<nums[m]<nums[r]:
                return nums[l]
            
            # if m < l,r move r down; update lower val (r) to lower midpoint
            elif nums[m] < nums[r]:
                
                r = m - 1
            # if m > l,r move l up; update higher val (l) to higher midpoint
            else:
                l = m + 1
        return minVal

        