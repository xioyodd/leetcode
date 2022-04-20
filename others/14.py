class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s1 = min(strs)
        s2 = max(strs)
        while not s1.startswith(s2):
            s2 = s2[:-1]
        return s2
        