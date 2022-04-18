class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        res = 0
        for c in s:
            if c != ' ':
                res+=1
            elif res != 0 and c == ' ':
                return res
        return res