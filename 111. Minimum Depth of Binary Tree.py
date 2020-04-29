# min(minDepth(left), minDepth(right)) + 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        Q, c = [root], []
        depth = 1
        
        while Q:
            node = Q.pop()
            if not node.left and not node.right:
                break
            
            c.append(node.left) if node.left else None
            c.append(node.right) if node.right else None

            if not Q and c:
                depth += 1
                Q = c
                c = []
        return depth
    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return min(left, right) + 1
        return 1 + max(left, right)