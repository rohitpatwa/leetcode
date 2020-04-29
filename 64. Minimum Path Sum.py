# DP problem. Keep storing the  minPathSum([i-1][j], [i][j-1]). We can go top down using recursion or bottom up using iterative.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.dp = [[False]*n for _ in range(m)]
        self.dp[0][0] = grid[0][0]
        return self.mps(grid, m-1, n-1)
        
    def mps(self, grid, i, j):
        p1, p2 = float('max'), float('max')
        if self.dp[i][j] is not False:
            return self.dp[i][j]
        if i > 0:
            p1 = self.mps(grid, i-1, j)
        if j > 0:
            p2 = self.mps(grid, i, j-1)
        
        self.dp[i][j] = grid[i][j] + min(p1, p2)
        return self.dp[i][j]
        

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue
                if i-1 < 0:
                    grid[i][j] += grid[i][j-1]
                elif j-1 < 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[i][j]