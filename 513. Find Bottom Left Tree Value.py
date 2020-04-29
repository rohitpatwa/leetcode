# Two ways to solve it. Either do preorder traversal by going root, right, left. Or do recursive call and find deepest elem of left tree and right tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         Q = [root]
        
#         while Q:
#             root = Q[0]
#             Q = Q[1:]
#             if root.right:
#                 Q.append(root.right)
#             if root.left:
#                 Q.append(root.left)
#         return root.val
            
        
        
        
        res = self.helper(root, 0)
        return res[1]
        
        
    def helper(self, node, level):
        if not node:
            return (-1, None)
        
        if not node.left and not node.right:
            return (level, node.val)
        
        leftMin = self.helper(node.left, level+1)
        rightMin = self.helper(node.right, level+1)
        
        if leftMin[0] > rightMin[0]:
            return leftMin
        elif leftMin[0] < rightMin[0]:
            return rightMin
        else:
            return leftMin
        