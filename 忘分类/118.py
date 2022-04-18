class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(numRows-1):
            tmp = [1]
            for j in range(i):
                tmp.append(res[i][j]+res[i][j+1])
            tmp.append(1)
            res.append(tmp)
        return res
