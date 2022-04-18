class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_n = None
        index = 0
        for i in nums:
            if i != pre_n:
                nums[index] = i
                pre_n = i
                index += 1
        return index