# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import Queue
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        current_list = []
        q = Queue.Queue()
        q.put(root)
        size = 1
        while size > 0:
            node = q.get()
            current_list.append(node.val)
            if node.left :
                q.put(node.left)
            if node.right:
                q.put(node.right)
            size -= 1
            if size == 0:
                result.append(current_list)
                current_list = []
                size = q.qsize()
        return result[::-1]