# Do level order traversal. At each step, insert the last value to result array.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        Q, c, res = [root], [], [root.val]
        
        while Q:
            node = Q.pop(0)
            if node.left:
                c.append(node.left)
            if node.right:
                c.append(node.right)
            if not Q:
                if c:
                    res.append(c[-1].val)
                Q = c
                c = []
        return res
            
                
                
        