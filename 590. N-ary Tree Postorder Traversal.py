# Implement a stack. Keep inserting children in stack and root.val in output arr. return arr[::-1]


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        
        stack = [root]
        res = []
        while stack:
            temp = stack[-1]
            stack = stack[:-1]
            res.insert(0, temp.val)
            for c in temp.children:
                stack.append(c)
                
        return res
        