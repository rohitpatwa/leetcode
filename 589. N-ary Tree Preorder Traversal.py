# Use stack. Keep adding current values to result list and reverse of children to stack

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        
        while stack:
            
            curr = stack[0]
            stack = stack[1:]
            
            res.append(curr.val)
            # print(q, curr.val)
            stack = curr.children + stack
        
        return res