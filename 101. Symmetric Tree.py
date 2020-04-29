# isMirror(root, root). Call recursively isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left) and t1.val==t2.val. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.isMirror(root, root)
        
    def isMirror(self, t1, t2):
        if not t1 and not t2:
            return True
        if (t1 and not t2) or (not t1 and  t2):
            return False
        
        if (t1.val==t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left):
            return True
        return False
        
        
