class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicate = 0
        missing = 0
        for n in nums:
            if n in seen:
                duplicate = n
            seen.add(n)
        for n in range(len(nums) + 1):
            if n not in seen:
                missing = n
        return [duplicate, missing]
