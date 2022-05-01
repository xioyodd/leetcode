# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        res_size = n * n
        up_bound = left_bound = 0
        down_bound = right_bound = n - 1
        count = 1
        while True:
            for j in range(left_bound, right_bound + 1):
                matrix[up_bound][j] = count
                count += 1
            up_bound += 1
            if count > res_size:
                break
            for i in range(up_bound, down_bound + 1):
                matrix[i][right_bound] = count
                count += 1
            right_bound -= 1
            if count > res_size:
                break
            for j in range(right_bound, left_bound - 1, -1):
                matrix[down_bound][j] = count
                count += 1
            down_bound -= 1
            if count > res_size:
                break
            for i in range(down_bound, up_bound - 1, -1):
                matrix[i][left_bound] = count
                count += 1
            left_bound += 1
            if count > res_size:
                break
        return matrix