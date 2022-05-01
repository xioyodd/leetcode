# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素
# 这题写的时候花了不少时间，思路不太清晰
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        res_size = m * n
        up_bound = left_bound = 0
        down_bound = m - 1
        right_bound = n - 1
        res = []
        while True:
            for j in range(left_bound, right_bound + 1):
                res.append(matrix[up_bound][j])
            up_bound += 1
            if len(res) >= res_size:
                break
            for i in range(up_bound, down_bound + 1):
                res.append(matrix[i][right_bound])
            right_bound -= 1
            if len(res) >= res_size:
                break
            for j in range(right_bound, left_bound - 1, -1):
                res.append(matrix[down_bound][j])
            down_bound -= 1
            if len(res) >= res_size:
                break
            for i in range(down_bound, up_bound - 1, -1):
                res.append(matrix[i][left_bound])
            left_bound += 1
            if len(res) >= res_size:
                break
        return res
