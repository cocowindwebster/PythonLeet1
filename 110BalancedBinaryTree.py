# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.__checkBalanced__(root) < 0:
            return False
        else:
            return True
        #return not (self.__checkBalanced__(root) == -1)

    def __checkBalanced__(self, root): #private function
        if root == None:
            return 0
        else:
            left = self.__checkBalanced__(root.left)
            right = self.__checkBalanced__(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1


