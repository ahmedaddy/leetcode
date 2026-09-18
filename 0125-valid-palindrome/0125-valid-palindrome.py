
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ""
        for c in s:
            if c.isalnum():
                st += c.lower()
        if st == st[::-1]:
            return True
        return False