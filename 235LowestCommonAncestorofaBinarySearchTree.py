# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# #Solution 1
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         smaller = p
#         larger = q
#         if p.val > q.val:
#             smaller = q
#             larger = p
#         while root != None:
#             if root.val < smaller.val:
#                 root = root.right
#             elif root.val > larger.val:
#                 root = root.left
#             else:
#                 return root;
#         return None;

# Solution 2:
# Python Ternary Expression
# (falseValue, trueValue)[test]
# Note: The FIRST PART is falseValue, the SECOND PART is trueValue
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root != None and (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[root.val < p.val]
        return root;

