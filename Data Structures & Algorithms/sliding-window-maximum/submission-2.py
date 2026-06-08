class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_map={}
        maximum=float("-inf")
        for n in nums[:k]:
            window_map[n]=window_map.get(n,0)+1
            maximum=max(maximum,n)
        res=[maximum]
        if k == len(nums):
            return res
        print(window_map)        
        for l in range(1,len(nums)-k+1):
            r=l+k-1
            c=nums[r]
            window_map[nums[l-1]]-=1
            if window_map[nums[l-1]]==0:
                window_map.pop(nums[l-1])
            window_map[c]=window_map.get(c,0)+1
            print(window_map)
            maximum=max(list(window_map))
            res.append(maximum)
        return(res)
