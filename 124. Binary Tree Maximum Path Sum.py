# Create a helper function get_sum which will get max sum till that node. Update res in get_sum with get_sum(left) + get_sum(right) + node.val.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.res = float('-inf')
        def get_sum(root):
            if root is None:
                return 0
            else:
                ls = max(get_sum(root.left), 0)
                rs = max(get_sum(root.right), 0)
                self.res = max(self.res, ls + rs + root.val)
                return max(ls, rs, 0) + root.val
        
        get_sum(root)
        return self.res