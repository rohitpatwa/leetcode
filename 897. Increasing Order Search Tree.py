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
