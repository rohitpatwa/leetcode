# This solution is in O(n) space. Do level order traversal and create links within the level.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        Q, c = [root], []
        
        while Q:
            curr = Q.pop(0)
            if Q:
                curr.next = Q[0]
                
            if curr.left:
                c.append(curr.left)
            if curr.right:
                c.append(curr.right)
            
            if not Q and c:
                Q = c
                c = []
            
        return root