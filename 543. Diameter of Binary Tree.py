# Diameter is max(diameter_left, diameter_right, left_depth+right_depth+1). Resurse on left and right subtrees. Return diam and depth at each step.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: 
            return 0 
        return self.dfs(root)[1]
    
    
    def dfs(self, node):
            if not node: 
                return (0, 0)
            depth_left, diam_left = self.dfs(node.left)
            depth_right, diam_right = self.dfs(node.right)
            return 1 + max(depth_left, depth_right), max(diam_left, diam_right, depth_left+depth_right)