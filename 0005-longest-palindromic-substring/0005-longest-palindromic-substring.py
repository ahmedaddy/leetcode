class Solution:
    def is_palindrom(self, s: str) -> bool:
        return s == s[::-1]
    def longestPalindrome(self, s: str) -> str:
        if self.is_palindrom(s):
            return s
        best = ""
        for i in range(0, len(s)):
            for j in range(i, len(s) + 1):
                if s[i:j] and self.is_palindrom(s[i:j]):
                    if len(best) < len(s[i:j]):
                        best = s[i:j]
        return best