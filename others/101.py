# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def same(self, l, r):
        if l == None and r == None:
            return True
        elif l == None or r == None or l.val != r.val:
            return False
        else:
            return self.same(l.left,r.right) and self.same(l.right, r.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.same(root.left,root.right)
        