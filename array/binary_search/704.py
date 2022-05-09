# 给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1

        return -1
