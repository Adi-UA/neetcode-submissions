class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(lst):
            curr,prev=lst[0],0
            for i in range(1,len(lst)):
                tmp=curr
                curr=max(curr,prev+lst[i])
                print(i,curr)
                prev=tmp
            return curr
        return max(helper(nums[1:len(nums)]),
                    helper(nums[:len(nums)-1])
                    )
        