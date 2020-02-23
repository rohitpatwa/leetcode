# Recursively check if left subtree and right subtee are univals

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        left_unival = (not root.left) or (root.val == root.left.val and self.isUnivalTree(root.left))
        right_unival = (not root.right) or (root.val == root.right.val and self.isUnivalTree(root.right))
        return left_unival and right_unival