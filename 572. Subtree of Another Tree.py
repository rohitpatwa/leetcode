# Traverse tree a and at each node check if it is equal to tree b. OR Traverse tree a and b and store in strings with delimeters. check if b in a.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val==b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right) 

        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        
        
class Solution:
    def traverseTree(self,root,res):
        if(not root):
            res.append("_")
            return
        res.append("#"+str(root.val))
        self.traverseTree(root.left,res)
        self.traverseTree(root.right,res)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        str_main =[]
        self.traverseTree(s,str_main)
        
        
        str_sub=[]
        self.traverseTree(t,str_sub)
        
        
        if("".join(str_sub) in "".join(str_main)):
            return True
        return False