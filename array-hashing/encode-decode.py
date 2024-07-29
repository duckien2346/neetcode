from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + 'A' + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        while s != '':
            i = s.index('A')
            l = int(s[:i])
            item = s[i+1:i+1+l]
            strs.append(item)
            s = s[i+1+l:]
        return strs

strs = ['neet', '','code','love','you']
strs = ['']
strs = ['1234', '132,1234', '1234\'']
strs = ['juu#aeu', '','code','love','you']
strs = []
resolve = Solution()
encode = resolve.encode(strs)
decode = resolve.decode(encode)
print(strs)
print(encode)
print(decode)
print(strs == decode)
