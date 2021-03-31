# Iterate BST as BS and at each point check of min diff and update the closest val.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.m, self.val = float('inf'), None
        self.helper(root, target)
        return self.val
    
    def helper(self, node, t):
        if not node:
            return
        if abs(t-node.val) < self.m:
            self.m = abs(t-node.val)
            self.val = node.val
        if t < node.val:
            return self.helper(node.left, t)
        elif t > node.val:
            return self.helper(node.right, t)
        
        
        
        