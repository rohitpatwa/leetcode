# Create an adjacency list. Find all the leaves. Trim leaves, remove connections and update new leaves till you reach center. 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        """
        In this approach we pick a random node x.
        We find the node furtheast to x i.e. y.
        The we find the node furthest to y i.e. z.
        Node in the middle from y to z is our desired node.
        """
        
        if n<=2:
            return list(range(n))
        
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        def max_path(node, visited):
            visited.add(node)
            paths = [max_path(n, visited) for n in adj[node] if n not in visited]
            path = max(paths or [[]], key=len) 
            path.append(node)
            return path
        
        x = 0
        path = max_path(x, set())  # path is in reverse order i.e. y to x
        y = path[0]
        path = max_path(y, set())
        
        if len(path)%2==1:
            return [path[len(path)//2]]
        else:
            return [path[len(path)//2 - 1], path[len(path)//2]]       
        
        
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        In this approach, we find the leaves and keep trimming the leaves
        till we reach the center.
        """        
        
        
        if n<=2:
            return list(range(n)) 
        
        adj = [set() for _ in range(n)]
        
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        leaves = [i for i in range(n) if len(adj[i])==1]
        
        while n>2:
            new_leaves = []
            n -= len(leaves)
            
            for leaf in leaves:
                connection = adj[leaf].pop()
                adj[connection].remove(leaf)
                
                if len(adj[connection])==1:
                    new_leaves.append(connection)
            leaves = new_leaves
            
        return leaves
