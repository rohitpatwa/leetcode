# Compare values of current nodes and recursively call left sub tree and right sub tree. Write proper break condition.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)