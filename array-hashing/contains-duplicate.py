from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = {}
        for num in nums:
            if hashSet.get(num):
                return True
            hashSet[num] = True
        return False

nums = [1, 2, 3, 3]
resolve = Solution()
result = resolve.hasDuplicate(nums)
print(result)
