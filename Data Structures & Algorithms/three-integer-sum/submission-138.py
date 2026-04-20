class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort values
        nums.sort()

        # check at each i at the start
        out = []
        for i, a in enumerate(nums):
            # skip if a[i] is equal to a[i-1]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            # otherwise check twosum
            while l < r:
                curr_sum = a + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    out.append([a, nums[l], nums[r]])
                    l += 1 # check for more
                    # skip if nums[l] = nums[l-1] until not equal
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return out

        # [-4,2,2]
        # [-4,1,3]
        # [-4,-4,2,2,1,3] -> [-4,-4,1, 2,2,2,2,3]
                

        