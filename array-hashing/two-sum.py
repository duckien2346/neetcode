from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l): 
            if nums[i] > target:
                continue
            for j in range(i+1, l):
                if nums[j] > target:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [0, 0]
        
nums = [3,5,4,6]
target = 7
resolve = Solution()
result = resolve.twoSum(nums, target)
print(result)
