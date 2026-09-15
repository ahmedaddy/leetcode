class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            for j, sn in enumerate(nums):
                if n + sn == target and i != j:
                    return [i, j]
        