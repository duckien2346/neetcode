from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if not dic.get(key):
                dic[key] = []
            dic[key].append(str)

        return list(dic.values())

strs = ["act","pots","tops","cat","stop","hat"]
resolve = Solution()
result = resolve.groupAnagrams(strs)
print(result)
