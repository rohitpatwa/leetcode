# Can be solved in both recursive and iterative ways. Iterate with BST nodes and return root where the value matches. Write the base case.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val==val:
            return root
        if root.val<val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        
        


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val==val:
                return root
            if root.val<val:
                root=root.right
            else:
                root = root.left
        return None