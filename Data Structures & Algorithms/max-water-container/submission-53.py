class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Go though each position starting from ends
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            print(f"i: {l}")
            # solve for area
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            print(f"max_area: {max_area}")
            
            # increment left forward if h1 < h2
            if heights[l] < heights[r]:
                l += 1
            # increment right backward if h2 < h1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max_area
            



        