# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True        
        return False if self.helper(root)==-1 else True
        
    def helper(self, node):
        if not node:
            return 0
        
        left_height = self.helper(node.left)
        if left_height == -1:
            return -1
        
        right_height = self.helper(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
        