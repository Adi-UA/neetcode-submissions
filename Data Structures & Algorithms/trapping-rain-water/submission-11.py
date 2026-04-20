class Solution:
    def trap(self, height: List[int]) -> int:
        # trapped water is a non-decreasing area going inward when 
        # boundaries are updated at max and height at each inside point is 0.
        # therefore, seek max boundaries and subtract out height
        # area at each point: min(max_l, max_r) - height[i]

        
        # start at end
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        total_water = 0
        while l < r:
            # increment to search for max boundaries
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                total_water += max(0, max_l - height[l]) # add water
            else:
                r -= 1
                max_r = max(max_r, height[r])
                total_water += max(0, max_r - height[r]) # add water
                
            
        return total_water
            
