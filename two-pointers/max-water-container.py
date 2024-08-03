from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, (len(heights) - 1)
        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area
                
height = [1,7,2,5,4,7,3,6]
height = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
resolve = Solution()
result = resolve.maxArea(height)
print(result)
