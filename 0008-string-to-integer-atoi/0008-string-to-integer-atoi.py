class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        sign = 1
        s = s.strip()
        if len(s) > 0:
            if s.strip()[0] == "-":
                sign = -1
            if s[0] == "-" or s[0] == "+":
                s = s[1:]
        for c in s:
            if c.isdigit():
                r = r * 10 + int(c)
            else:
                break
        if r * sign >= 2147483648:
            return 2147483647
        if r * sign < -2147483647:
            return -2147483648
        return r * sign
