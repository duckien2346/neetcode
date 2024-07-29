from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)
        max_freq = max(dic.values())
        freq = [[] for i in range(max_freq + 1)]
        for num, count in dic.items():
            freq[count].append(num)
        result = []
        for i in range(max_freq, 0, -1):
            result.extend(freq[i])
            if len(result) > k:
                return result[:k]
        return result;

nums = [7,7]
k = 2
resolve = Solution()
result = resolve.topKFrequent(nums, k)
print(result)
