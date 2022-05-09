# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回[-1, -1]。
# 进阶：
# 你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
# [1] 1
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def search_left_bound(nums, target):
            l = 0
            r = len(nums) - 1
            while l<=r:
                mid = l + (r-l)//2
                if target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if l == len(nums) or nums[l] != target:  #r == -1 or 是不需要的
                return -1
            return l


        def search_right_bound(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            if r == -1 or nums[r] != target: # l == len(nums)是可能对的
                return -1
            return r

        l = search_left_bound(nums,target)
        if l==-1:
            return [-1,-1]
        r = search_right_bound(nums,target)
        return [l,r]