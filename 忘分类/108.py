# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        lenth = len(nums)
        if lenth == 0:
            return None
        m = lenth//2
        ret = TreeNode(val = nums[m])
        ret.left = self.sortedArrayToBST(nums[:m])
        ret.right = self.sortedArrayToBST(nums[m+1:])
        return ret