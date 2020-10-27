# LCA returns a node if it finds at least 1 of p and q in given tree. If we find 1 node in left tree and 1 in right sub tree, return root.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        lowestCommonAncestor returns a node if it finds at least one node amongst
        p and q in the given sub tree.
        If we find a node in left sub tree and one in right sub tree,
        we return the current node. If one of them is none, the other 
        sub tree contains the result. Return the answer returned from 
        the other subtree.
        """

        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
                                         
        if left and right:
            return root
                                         
        if left:
            return left
        
        if right:
            return right