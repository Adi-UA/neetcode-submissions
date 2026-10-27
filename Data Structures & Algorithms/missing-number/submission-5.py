class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        expected=int((len(nums)+1)*(len(nums)/2))
        return expected-total