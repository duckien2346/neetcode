from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            target = 0 - nums[i]
            (l,r) = (i+1, length-1)
            while l<r:
                current_sum = nums[l]+nums[r]
                if current_sum<target:
                    l+=1
                elif current_sum>target:
                    r-=1
                else:
                    arr = [nums[i], nums[l], nums[r]]
                    if not arr in result:
                        result.append(arr)
                    l+=1
                    r-=1
        return result
        
nums=[0,1,1]
nums=[-1,0,1,2,-1,-4]
nums=[3,0,-2,-1,1,2]
resolve = Solution()
result = resolve.threeSum(nums)
print(result)
