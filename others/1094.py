# 先下后上0—1-2-3-4-5-

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
        self.max = 0
        for i in self.diff:
            pre_num += i
            res.append(pre_num)
        return res


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        nums = [0] * 1000
        df = Difference(nums)
        for val,i,j in trips:
            df.increment(i,j-1,val)

        
        if max(df.result()) > capacity:
            return False
        return True