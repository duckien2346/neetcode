from typing import List
from operator import mul
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        i = len(nums) - 1
        temp = nums[i]
        i -= 1
        while i >= 0:
            result[i] *= temp
            temp *= nums[i]
            i -= 1
        return result
        
strs = [1,2,4,6]
resolve = Solution()
result = resolve.productExceptSelf(strs)
print(result)
