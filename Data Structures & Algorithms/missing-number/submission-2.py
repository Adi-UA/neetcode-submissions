class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=0
        for n in nums:
            total+=n
        n=len(nums)
        expected=int((n+1)*(n/2))
        return expected-total