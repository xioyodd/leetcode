# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depth(self, root):
        if root == None:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        if l==-1 or r ==-1 or l-r > 1 or r-l >1:
            return -1
        return max(l,r)+1
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.depth(root) == -1:
            return False
        return True