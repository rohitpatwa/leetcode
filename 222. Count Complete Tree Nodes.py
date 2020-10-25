# Find len of tree by going max left. Do binary search (similar to finding first bad version/last good version) to find num of nodes in last level.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def get_len(self, root):
        """root has len = 1, None has len = 0"""
        if not root:
            return 0
        l = 0
        while root:
            l += 1
            root = root.left
        return l
    
    def exists(self, root, num, l):
        """calls recursively with left or right child of root,
           updated num depending on whether we go left or 
           right and, l-1.
        """
        if l==2:  # base case: we have reached second last level
            if (num==1 and root.left) or (num==2 and root.right):
                return True
            else:
                return False
        
        if num <= 2**(l-1)/2:  
            # num <= half of max nodes in last level of curr subtree
            # recursively call left subtree with num and l-1
            return self.exists(root.left, num, l-1)
        else:
            # num > half of max nodes in last level of curr subtree
            # recursively call right subtree with (num - half of max nodes in last level)  and l-1
            return self.exists(root.right, num - 2**(l-1)/2, l-1)
        
    def isComplete(self, root, l):
        """checks if a given tree is filled to its max capacity
        """
        while l and root:
            root = root.right
            l -= 1 
        return l==0
        
    
    def countNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        l = self.get_len(root)
        
        if self.isComplete(root, l):
            return 2**(l) - 1
        
        nodes_till_second_last = 2**(l-1) - 1
        
        min_nodes_in_last, max_nodes_in_last = 1, 2**(l-1)
        
        # analogous to finding first bad version 
        while min_nodes_in_last < max_nodes_in_last:
            
            mid = (min_nodes_in_last + max_nodes_in_last)//2
            
            if self.exists(root, mid, l):    
                min_nodes_in_last = mid + 1
            else:
                max_nodes_in_last = mid
        
        nodes_in_last_level = min_nodes_in_last - 1
        
                
        return nodes_till_second_last + nodes_in_last_level
        