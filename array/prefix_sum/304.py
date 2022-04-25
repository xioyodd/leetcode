# 给定一个二维矩阵 matrix，以下类型的多个请求：
#
# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1,col1) ，右下角 为 (row2,col2) 。
# 实现 NumMatrix 类：
#
# NumMatrix(int[][] matrix)给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2)返回 左上角 (row1,col1)、右下角(row2,col2) 所描述的子矩阵的元素 总和 。


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.pre_sum = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(1,len(self.pre_sum)):
            for j in range(1,len(self.pre_sum[0])):
                self.pre_sum[i][j] = matrix[i-1][j-1] + self.pre_sum[i-1][j] + self.pre_sum[i][j-1] - self.pre_sum[i-1][j-1]




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.pre_sum[row2+1][col2+1] - self.pre_sum[row1][col2+1] - self.pre_sum[row2+1][col1] + self.pre_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)