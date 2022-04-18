class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1, 1]
        i=2
        while i<=n:
            res.append(res[i-1] + res[i-2])
            i+=1
        return res[n]