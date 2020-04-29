# Take abs value of current node and add ot to an on going sum and sibtract 1 from that sum at the very end	

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.moves = 0
        self.helper(root)
        return self.moves
        
        
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.moves += abs(left) + abs(right)
        return node.val + left + right -1