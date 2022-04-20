# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        lst_l = self.inorderTraversal(root.left)
        lst_m = [root.val]
        lst_r = self.inorderTraversal(root.right)
        return lst_l + lst_m + lst_r