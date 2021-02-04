# Normal levelorder traversal. Flag to track direction. When appending temp to res, check flag to append temp or trmp[::-1].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        Q, c  = deque([root]), deque()
        
        res, temp = [], []
        
        left = True
        
        while Q:
            curr = Q.popleft()
            temp.append(curr.val)
            
            
            if curr.left:
                c.append(curr.left)
            if curr.right:
                c.append(curr.right)
                
            if not Q:
                if left:
                    res.append(temp)
                else:
                    res.append(reversed(temp))
                left = not left
                Q, c, temp = c, deque(), []

        return res
