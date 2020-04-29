# Nested while loops. Use a stack and curr node. Push all left nodes in stack iteratively. When curr is null, start popping and push right in stack.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            stack = stack[:-1]
            res.append(curr.val)
            curr = curr.right
        return res