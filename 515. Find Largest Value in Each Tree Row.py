# Maintain two lists, one Q and C(for it's children). When Q is empty, take the max of children and make Q=C and C=[].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = [root.val]
        q = [root]
        c = []
        
        while q:
            node = q.pop()
            if node.left:
                c.append(node.left)
            if node.right:
                c.append(node.right)
            
            if not q and c:
                q = c
                res.append(max([x.val for x in c]))
                c = []
    
        return res