# Do BFS. When you reach a null node, check if the Q is empty. If yes: return True else return False

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        Q = [root]
        
        while Q:
            node = Q.pop()
            if not node:
                if any(Q):
                    return False
                else:
                    return True
            Q.insert(0, node.left)
            Q.insert(0, node.right)
        return True
            