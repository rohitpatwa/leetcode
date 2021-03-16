# DFS or BFS on BT starting from root. Every child is given value as per formula. Add values to a set. Search target in set.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        Q = [root]
        self.vals = set([0])
        while Q:
            node = Q.pop()
            if node.left:
                node.left.val = 2*node.val + 1
                self.vals.add(2*node.val + 1)
                Q.insert(0, node.left)
            if node.right:
                node.right.val = 2*node.val + 2
                self.vals.add(2*node.val + 2)
                Q.insert(0, node.right)
        self.root = root

    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)



# Approach 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = set()
        self.preOrder(root, 0)
        
        
    def preOrder(self, node, val):
        if not node:
            return
        
        self.vals.add(val)
        self.preOrder(node.left, 2*val+1)
        self.preOrder(node.right, 2*val+2)

    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)