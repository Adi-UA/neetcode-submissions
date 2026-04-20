class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort values
        nums.sort()
        print(nums)

        # check at each i at the start
        i = 0 
        l = i + 1
        out = []
        while i < len(nums) - 2:
            # start twosum
            l = i + 1
            r = len(nums) - 1
            # skip if a[i] is equal to a[i-1] or greater than 0
            if i > 0:
                if nums[i] == nums[i-1] or nums[i] > 0:
                    i += 1
                    continue
            # otherwise check twosum
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    # skip if nums[l] = nums[l-1]
                    if l > i + 1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
            i += 1
        return out

        # [-4,2,2]
        # [-4,1,3]
        # [-4,-4,2,2,1,3] -> [-4,-4,1, 2,2,2,2,3]
                

        