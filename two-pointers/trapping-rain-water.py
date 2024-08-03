from contextlib import contextmanager
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # area = 0
        # for i in range(1, len(height)-1):
        #     max_left = max(height[:i])
        #     max_right = max(height[i+1:])
        #     area += max(0, min(max_left, max_right) - height[i])
        # return area
        area = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                pass
                l += 1
                leftMax = max(leftMax, height[l])
                area += leftMax - height[l]
            else:
                pass
                r -= 1
                rightMax = max(rightMax, height[r])
                area += rightMax - height[r]
        return area
                        
height = [0,2,0,3,1,0,1,3,2,1]
resolve = Solution()
result = resolve.trap(height)
print(result)
