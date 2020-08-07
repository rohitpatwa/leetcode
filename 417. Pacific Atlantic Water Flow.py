# Create 2 sets P and A for nodes covered by both seas. Perform dfs from all rows and cols of P and A. Return intersecrion of P and A.

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        P, A = set(), set()
        
        for i in range(m):
            self.dfs(i, 0, P, matrix)
            self.dfs(i, n-1, A, matrix)
            
        for i in range(n):
            self.dfs(0, i, P, matrix)
            self.dfs(m-1, i, A, matrix)
            
        return [list(i) for i in (P & A)]

    def dfs(self, i, j, visited, matrix):
        visited.add((i,j))
        m, n = len(matrix), len(matrix[0])
        
        for (a,b) in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
            if 0<=a<m and 0<=b<n and matrix[a][b] >= matrix[i][j] and (a,b) not in visited:
                self.dfs(a, b, visited, matrix)