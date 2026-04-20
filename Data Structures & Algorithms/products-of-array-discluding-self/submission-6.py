class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_i = []
        total_mult = 1
        # get complete product
        for i, n in enumerate(nums):
            # track zero indices
            if n == 0:
                zero_i.append(i)
            else:
                total_mult *= n

            # stop when encountering 2 zeros
            if len(zero_i) > 1:
                return [0] * len(nums)
            
            
        
        # if only 1 zero, return list of 0's with the index of the 0 replaced
        # with the total multiple
        if len(zero_i) == 1:
            out = [0] * len(nums)
            out[zero_i[0]] = total_mult
            return out

        out = []
        # if no zeros: go through each number and divide from total
        for n in nums:
            out.append(int(total_mult / n))
        
        return out
        