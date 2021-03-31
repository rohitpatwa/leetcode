# Do BFS. Store info of (node, pos_from_left, depth). Whenever depth changes, store it as leftmost pos. Find max pos_from_left - pos.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        Q = deque([(root, 0, 0)])  # node, pos in list, depth 
        curr_depth = 0
        max_width = 0
        left_pos = 0
        
        while Q:
            node, pos, depth = Q.popleft()
        
            if node.left:
                Q.append((node.left, 2*pos+1, depth+1))  # 2*pos+1 because left child
            if node.right:
                Q.append((node.right, 2*pos+2, depth+1))  # 2*pos+1 because right child
            
            if depth!=curr_depth:
                left_pos = pos
                curr_depth = depth
            
            max_width = max(max_width, pos - left_pos + 1)
        return max_width        