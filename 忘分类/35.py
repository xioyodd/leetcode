class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r :
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m-1
            elif target >nums[m]:
                l = m+1
        if target <= nums[l]:
            return l
        elif target > nums[l]:
            return l+1