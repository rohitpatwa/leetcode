# Check if if the subtrees contain 1. Recursively call on left and right subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def containsOne(node):
            if not node: 
                return False
            
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)

            if not a1: 
                node.left = None
            if not a2: 
                node.right = None

            if node.val==1 or a1 or a2:
                return True
            return False

        return root if containsOne(root) else None