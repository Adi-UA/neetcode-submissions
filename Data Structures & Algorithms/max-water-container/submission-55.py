class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # want to maximize width x height
        # width = l-r, height = min(heights[l],heights[r])
        
        # if only one value, no area
        if len(heights)==1:
            return 0
        
        # start with max width
        l,r=0,len(heights)-1
        maxarea=(r-l)*min(heights[l],heights[r])
        
        # try to maximize height now
        while l<r:
            # move the one that's smaller
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            maxarea=max(maxarea,(r-l)*min(heights[l],heights[r]))
        return maxarea
