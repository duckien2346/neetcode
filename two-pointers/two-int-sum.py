from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        (l, r) = (0, len(numbers)-1)
        while l < r:
            current_sum = numbers[l]+numbers[r]
            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []

numbers = [1,2,3,4]
target = 3
resolve = Solution()
result = resolve.twoSum(numbers, target)
print(result)
