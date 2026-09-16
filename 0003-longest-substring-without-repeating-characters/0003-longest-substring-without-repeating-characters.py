class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        current = ""
        best = 1
        for c in s:
            if c in current:
                if best < len(current):
                    best = len(current)
                current = current[current.index(c)+1:]
            current += c
        if best < len(current):
            best = len(current)
        return best
