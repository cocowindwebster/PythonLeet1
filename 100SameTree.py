# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q : #NOTE1: grammar
            return True
        elif not p or not q:  #NOTE2: use "elif" instead of "else if"
            return False
        elif p.val != q.val:
            return False
        else :
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

