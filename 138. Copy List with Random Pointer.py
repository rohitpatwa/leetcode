# Create a dictionary that keeps mapping of old nodes to new nodes. Then run a loop which places all next and random pointers.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None
        
        p = head
        old_to_new = {}
        
        while p:
            new = Node(p.val)
            old_to_new[p] = new
            p = p.next
            
        for old, new in old_to_new.items():
            new.next = old_to_new[old.next] if old.next in old_to_new else None
            new.random = old_to_new[old.random] if old.random in old_to_new else None
            
        return old_to_new[head]
            
            
        