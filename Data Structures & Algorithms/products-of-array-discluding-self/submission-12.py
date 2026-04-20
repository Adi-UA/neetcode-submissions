class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # METHOD 1: Division
        # total_mult = 1
        # no_zeros = 0
        # # get complete product
        # for i, n in enumerate(nums):
        #     # track zero indices
        #     if n == 0:
        #         no_zeros += 1
        #     else:
        #         # make running non-zero multiple
        #         total_mult *= n

        #     # stop when encountering 2 zeros
        #     if no_zeros > 1:
        #         return [0] * len(nums)

        # # create numeric output
        # out = []
        # for n in nums:
        #     # if a zero in original list, the output is mostly 0's
        #     if no_zeros == 1:
        #         if n == 0:
        #             # except when at the index with 0 in original list
        #             out.append(total_mult)
        #         else:
        #             out.append(0)
        #     else:
        #         # otherwise no zeros in original list: just divide out
        #         out.append(int(total_mult / n))
        
        # return out
        
        # METHOD 2:
        out = []
        fwd = 1
        bwd = 1
        for i in range(len(nums)):
            out.append(fwd)
            fwd *= nums[i]
            
        for j in range(len(nums)-1, -1 , -1):
            out[j] *= bwd
            bwd *= nums[j]
        return out