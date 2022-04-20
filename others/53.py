import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_sum = 0
        min_pre_sum = 0
        res = -sys.maxsize
        for i in nums:
            pre_sum += i
            res = max(res, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return res