class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # create tuple of i and num
        # pair = [(i,n) for i,n in enumerate(nums)]
        # while len(pair) > 0:
        #     #search halfway index
        #     half_i = (len(pair)-1) // 2
            
        #     #remove lower/upper half
        #     if pair[half_i][1] < target:
        #         pair = pair[half_i+1:]
        #     elif pair[half_i][1] > target:
        #         pair = pair[:half_i]
        #     else:
        #         return pair[half_i][0]
        # return -1
        

        # METHOD 2: TWO POINTERS
        l,r = 0, len(nums) - 1
        while l <= r:
            halfway = (l + r) // 2
            if nums[halfway] == target:
                return halfway
            elif nums[halfway] > target:
                r = halfway - 1
            else:
                l = halfway + 1
        return -1