# Simple recursive solution by DFS. call dfs with current sum. It will keep calling itself with left and right nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.sum = sum
        return self.helper(root, 0)

    
    def helper(self, node, s):
        if not node:
            return False
        s += node.val
        if not node.left and not node.right and s==self.sum:
            return True
        return self.helper(node.left, s) or self.helper(node.right, s)
