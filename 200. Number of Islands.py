# on every instance of 1, perform DFS and set all the conected ones to 0.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1':
                    count += 1
                    self.DFS(grid, r, c)
                    
        return count
    
    def DFS(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 
        
        if grid[i][j]=='0':
            return
        grid[i][j] = '0'
        self.DFS(grid, i+1, j)
        self.DFS(grid, i, j+1)
        self.DFS(grid, i-1, j)
        self.DFS(grid, i, j-1)
                        
                    