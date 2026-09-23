# Caching
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[0]*len(nums)
        def dfs(i):
            if lis[i]!=0:
                return lis[i]
            best=1
            for j in range(i+1,len(nums)):
                nums_i=0 if i==-1 else nums[i]
                if nums[j]>nums_i:
                    best=max(best,dfs(j)+1)
            lis[i]=best
            return lis[i]
        return max((dfs(i) for i in range(len(nums))), default=0)