class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        acc = 0
        best = 0
        for n in nums:
            if n == 1:
                acc += 1
            elif n == 0:
                if best < acc:
                    best = acc
                acc = 0
        if best < acc:
            best = acc
        return best