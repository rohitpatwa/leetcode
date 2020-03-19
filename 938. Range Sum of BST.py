# Check if root lies in the range, if True : recursively call left and right; add node.val, else : call left or right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        self.helper(root, L, R)
        return self.total
        
    def helper(self, node, L, R):
        if not node:
            return
        if node.val>=L and node.val<=R:
            self.total += node.val
            self.helper(node.left, L, R)
            self.helper(node.right, L, R)
        elif node.val < L:
            self.helper(node.right, L, R)
        else:
            self.helper(node.left, L, R)