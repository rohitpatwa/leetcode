# For each 1, count the number of surrounding 0's.

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perim = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if (i>0 and grid[i-1][j]==0) or i==0:
                        perim += 1
                    if (j>0 and grid[i][j-1]==0) or j==0:
                        perim += 1
                    if (i<m-1 and grid[i+1][j]==0) or i==m-1:
                        perim+=1
                    if (j<n-1 and grid[i][j+1]==0) or j==n-1:
                        perim+=1
        return perim

                        