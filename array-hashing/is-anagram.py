from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for c in s:
            if dic.get(c):
                continue
            if s.count(c) != t.count(c):
                return False
            dic[c] = True

        return True

s = "racecar"
t = "carrace"
resolve = Solution()
result = resolve.isAnagram(s, t)
print(result)
