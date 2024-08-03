class Solution:
    def isValid(self, s: str) -> bool:
        stack = list[str]()
        mapping = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if not c in mapping:
                stack.append(c)
            elif stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        return not stack

s = "[(])"
s = "[]"
s = "([{}])"
resolve = Solution()
result = resolve.isValid(s)
print(result)
