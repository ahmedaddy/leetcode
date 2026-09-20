class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        if x < 0:
            s = 1
            x *= -1
        x = int(str(x)[::-1])
        if x > 2147483648 or x < -2147483647:
            return 0
        if s == 1:
            return -int(x)
        else:
            return int(x)

