class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=0
        for num in nums:
            total+=num
        n=len(nums)
        expected=int((n+1)*(n/2))
        return expected-total