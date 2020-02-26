# Inorder traversal. Constant space. Inorder gives sorted values in BST.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = -9999
        self.min_diff = 9999
        self.helper(root)
        return self.min_diff
        
        
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        # print(self.prev, root.val)
        self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val
        self.helper(root.right)