class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        acc = 0
        prev = 0
        for c in reversed(s):
            if prev > roman[c]:
                acc -= roman[c]
            else:
                acc += roman[c]
            prev = roman[c]
        return acc