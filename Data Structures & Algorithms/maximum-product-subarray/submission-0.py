class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=float("-infinity")
        currMax=1
        currMin=1
        for n in nums:
            tmp=currMax
            currMax=max(n,currMax*n,currMin*n)
            currMin=min(n,tmp*n,currMin*n)
            maximum=max(maximum, currMax)
        return maximum