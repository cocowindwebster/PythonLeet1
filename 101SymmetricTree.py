# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSame(self, a, b):
        if a == None and b == None:
            return True
        elif a == None or b == None:
            return False
        elif a.val != b.val:
            return False
        else:
            return self.isSame(a.left, b.right) and self.isSame(a.right, b.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            #return isSame(root.left, root.right)   #ERROR1: Line 27: NameError: global name 'isSame' is not defined
            return self.isSame(root.left, root.right)

