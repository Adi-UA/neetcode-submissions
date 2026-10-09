class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn,mx=nums[0],nums[0]
        res=mx
        for n in nums[1:]:
            tmp=mn
            mn=min(mn*n,mx*n,n)
            mx=max(tmp*n,mx*n,n)
            res=max(mx,res)
        return res