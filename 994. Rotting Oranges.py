# Store all the rotten oranges in a Q. Perform BFS from multiple roots in the Q. Keep adding new rotten cells in Q. Check for fresh cell in the end. 


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Q = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    Q.append((i, j))
        
        res = -1 if Q else 0
        while Q:
            res += 1
            Q_size = len(Q)
            for _ in range(Q_size):
                rot = Q.pop()
                
                i, j = rot
                if i+1 < len(grid) and grid[i+1][j]==1:
                    grid[i+1][j] = 2
                    Q.insert(0, (i+1, j))
                if i-1 >= 0 and grid[i-1][j]==1:
                    grid[i-1][j] = 2
                    Q.insert(0, (i-1, j))
                if j+1 < len(grid[0]) and grid[i][j+1]==1:
                    grid[i][j+1] = 2
                    Q.insert(0, (i, j+1))
                if j-1 >= 0 and grid[i][j-1]==1:
                    grid[i][j-1] = 2
                    Q.insert(0, (i, j-1))
        
        for i in grid:
            for j in i:
                if j==1:
                    return -1
        return res