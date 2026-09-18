class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        res = ""
        for c in range(len(first)):
            carry = ""
            for s in range(len(strs)):
                try:
                    if first[c] != strs[s][c]:
                        return res
                except IndexError:
                    return res
                else:
                    carry += first[c]
            res += carry[0]
        return res
