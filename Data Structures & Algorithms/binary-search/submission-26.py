class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,u = 0, len(nums) -1        

        while l <= u:
            mid = (l + u) // 2
            mid_e = nums[mid]

            if target == mid_e:
                return mid
            elif target < mid_e:
                u = mid - 1
            else:
                l = mid + 1
        
        return -1