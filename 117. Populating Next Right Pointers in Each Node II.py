# This is O(1) space. Create parent, child and child_head nodes. Move parent node horizontally and create links in child nodes.

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
        parent = root
        child, child_head = None, None
        
        while parent:
            if parent.left:
                
                if not child_head:
                    child_head = parent.left
                
                if child:
                    child.next = parent.left
                child = parent.left
                    
            if parent.right:
                
                if not child_head:
                    child_head = parent.right
                
                if child:
                    child.next = parent.right
                child = parent.right
                    
            parent = parent.next
            if not parent:
                parent = child_head
                child, child_head = None, None
            
        return root