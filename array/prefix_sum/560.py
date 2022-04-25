# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_dict = {0:1}
        pre_sum_i = 0
        ret = 0
        for i in range(len(nums)):
            pre_sum_i += nums[i]
            pre_sum_j = pre_sum_i - k
            if pre_sum_j in pre_dict:
                ret += pre_dict[pre_sum_j]
            pre_dict[pre_sum_i] = pre_dict.get(pre_sum_i,0) + 1
        return ret