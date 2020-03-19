# Recursively call func on left_sub and right_sub. Attach flattened left_sub on right side, traverse it and then attach the flattened right_sub.

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        left_sub_tree = self.flatten(root.left)
        right_sub_tree = self.flatten(root.right)
        root.left = None
        root.right = left_sub_tree
        ptr = root
        while ptr.right:
            ptr = ptr.right
        ptr.right = right_sub_tree
        return root



# Craete a stack S with root in it. curr = S.pop(). Add right, left child. S.peek() and add it to right of curr.

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        S = [root]
        
        while S:
            curr = S.pop()
            if curr.right:
                S.append(curr.right)
            if curr.left:
                S.append(curr.left)        
            if S:
                curr.right = S[-1]
            curr.left = None
        return root