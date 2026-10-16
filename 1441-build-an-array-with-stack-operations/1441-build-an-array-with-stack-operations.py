class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        register = []
        i = 0
        for num in range(n):
            if num + 1 in target:
                register.append("Push")
                i += 1
            else:
                register.append("Push")
                register.append("Pop")
            if i == len(target):
                break
        return register