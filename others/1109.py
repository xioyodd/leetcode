class Difference(object):
    def __init__(self, nums):
        self.diff = []
        pre_num = 0
        for i in nums:
            self.diff.append(i - pre_num)
            pre_num = i
    
    def increment(self, i, j, val):
        self.diff[i] += val
        if len(self.diff) > j+1:
            self.diff[j+1] -= val

    def result(self):
        res = []
        pre_num = 0
        for i in self.diff:
            pre_num += i
            res.append(pre_num)
        return res

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        nums = [0] * n
        df = Difference(nums)
        for i,j,val in bookings:
            df.increment(i-1,j-1,val)
        return df.result()