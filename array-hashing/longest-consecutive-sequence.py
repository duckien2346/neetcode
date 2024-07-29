from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num-1 in nums_set:
                continue
            count = 1
            i = 1
            while num+i in nums_set:
                count += 1
                i += 1
            max_count = max([max_count, count])
        return max_count

nums = [1,2,3, 9,10,11,12]
nums = [1,2,20,4,10,3,4,5,-1,0]
nums = [2,20,4,10,3,4,5]
resolve = Solution()
result = resolve.longestConsecutive(nums)
print(result)
