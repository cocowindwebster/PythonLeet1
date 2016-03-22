from TreeNode import TreeNode
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
            return [""]
        each = [root.val]
        all = []
        self.dfs(root, each, all)
        return all

    def dfs(self, root, each, all):
        if root == None:
            return
        elif root.left == None and root.right == None:
            return all.append("->".join(str(x) for x in each))
        if root.left != None:
            each.append(root.left.val)
            self.dfs(root.left, each, all)
            each.pop()
        if root.right != None:
            each.append(root.right.val)
            self.dfs(root.right, each, all)
            each.pop()

def main():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    result = s.binaryTreePaths(root)
    print result

if __name__ == "__main__" :
    main()

