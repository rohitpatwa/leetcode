# Do in-order traversal and store elements. Make a tree from the stored elements.

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        self.lis = []
        self.dfs(root)

        root = TreeNode(-1)
        ptr = root
        
        for i in self.lis:
            ptr.right = TreeNode(i)
            ptr.left = None
            ptr = ptr.right
        return root.right
    
    def dfs(self, root):
        if not root:
            return None
        self.helper(root.left)
        self.lis.append(root.val)
        self.helper(root.right)



# Approach 2

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.dummy = TreeNode(-1)
        self.curr = self.dummy
        self.inOrder(root)
        return self.dummy.right
        
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        self.curr.right = TreeNode(node.val)
        self.curr = self.curr.right
        self.inOrder(node.right)