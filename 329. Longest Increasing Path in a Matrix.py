# Simple solution. Perform DFS at each cell with memoization. DFS will return max path starting at that cell.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        self.dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if not self.dp[i][j]:
                    self.dp[i][j] = self.DFS(matrix, i, j, m, n)
                
        return max(max(y) for y in self.dp)
    
    def DFS(self, matrix, i, j, m, n):
        
        org = matrix[i][j]
        
        cands = [0]
        
        for a,b in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
            if 0<=a<m and 0<=b<n and matrix[a][b] is not None and matrix[a][b] > org:
                if not self.dp[a][b]:
                    self.dp[a][b] = self.DFS(matrix, a, b, m, n)
                cands += [self.dp[a][b]]
        
        return max(cands) + 1