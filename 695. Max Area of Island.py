# Visit every loc in grid. If loc==1, set it to zero and perform BFS by setting it's neighbors 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        self.m, self.n = len(grid), len(grid[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j]:
                    area = self.calc_area(grid, i, j)
                    max_area = max(max_area, area)
        
        return max_area
                
                
    def calc_area(self, grid, i, j):
        
        area = 0
        Q = [[i, j]]
        grid[i][j] = 0
        
        while Q:
            
            a, b = Q.pop(0)
            area += 1
            
            if a-1>=0 and grid[a-1][b]:
                Q.append([a-1, b])
                grid[a-1][b] = 0
            if b+1<self.n and grid[a][b+1]:
                Q.append([a, b+1])
                grid[a][b+1] = 0
            if a+1<self.m and grid[a+1][b]:
                Q.append([a+1, b])
                grid[a+1][b] = 0
            if b-1>=0 and grid[a][b-1]:
                Q.append([a, b-1])
                grid[a][b-1] = 0
        
        return area
        