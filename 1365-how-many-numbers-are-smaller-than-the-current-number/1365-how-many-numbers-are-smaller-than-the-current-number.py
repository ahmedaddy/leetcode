class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            found = 0
            for j in range(len(nums)):
               if i != j and nums[i] > nums[j]:
                found += 1
            res.append(found)
        return res