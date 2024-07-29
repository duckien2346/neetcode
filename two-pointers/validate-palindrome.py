class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     formated_s = ''.join(item.lower() for item in s if item.isalnum())
    #     length = len(formated_s)
    #     for i in range(length//2):
    #         if formated_s[i] != formated_s[length-1 - i]:
    #             return False
    #     return True
    def isalnum(self, c: str) -> bool:
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'
    # not allocate memory
    def isPalindrome(self, s: str) -> bool:
        (l, r) = (0, len(s)-1)
        while l < r:
            while l<r and not self.isalnum(s[l]):
                l += 1
            while l<r and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

s="0P"
s = "Was it a car or a cat I saw?"
resolve = Solution()
result = resolve.isPalindrome(s)
print(result)
