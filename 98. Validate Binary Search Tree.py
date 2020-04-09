# Create a helper func which takes (node, lower_bound and upper_bound). Recursively call on left and right sub tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, -float('inf'), float('inf'))
    

    def validate(self, root, lb, ub):
        # lb = lower bound, ub = lower bound
        if not root:
            return True
        if root.val <= lb or root.val >= ub:
            return False
        return self.validate(root.left, lb, root.val) and self.validate(root.right, root.val, ub)