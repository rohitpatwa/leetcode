# Do BFS. Store info of (node, pos_from_left, depth). Whenever depth changes, store it as leftmost pos. Find max pos_from_left - pos.

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        Q = [(root, 0, 0)]
        curr_depth = 0
        max_width = 0
        left_pos = 0
        while Q:
            node, pos, depth = Q.pop()
            if node.left:
                Q.insert(0, (node.left, 2*pos+1, depth+1))
            if node.right:
                Q.insert(0, (node.right, 2*pos+2, depth+1))
            
            if depth!=curr_depth:
                left_pos = pos
                curr_depth = depth
            max_width = max(max_width, pos - left_pos + 1)
        return max_width
