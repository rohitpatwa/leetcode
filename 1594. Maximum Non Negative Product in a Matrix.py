# At each elem in dp grid store min and max prod till that elem. Take min and max of leftmin, leftmax, topmin, topmax.

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        # dp will be a grid of size m*n where each elem will be a tuple
        # each tuple will contain (min, max) which indicate min possible
        # product till that path and max possible product till that path
        dp = [[(0, 0)]*n for _ in range(m)]
        
        
        # Initialize first row and col of dp. In first row and col, there's no
        # choice so min and max will be same
        dp[0][0] = (grid[0][0], grid[0][0])
        
        for i in range(1, m):
            dp[i][0] = (grid[i][0] * dp[i-1][0][0], grid[i][0] * dp[i-1][0][1])

        for j in range(1, n):
            dp[0][j] = (grid[0][j] * dp[0][j-1][0], grid[0][j] * dp[0][j-1][1])
        
        
        # For every elem of dp, min will be min of 4 elems.
        # [left_min, left_max, top_min, top_max] * grid[i][j]. Same goes for max
        for i in range(1, m):
            for j in range(1, n):

                g = grid[i][j]
                                
                top = dp[i-1][j]
                left = dp[i][j-1]
                minimum = min([g*top[0], g*top[1], g*left[0], g*left[1]])    
                maximum = max([g*top[0], g*top[1], g*left[0], g*left[1]])
                    
                dp[i][j] = (minimum, maximum)
                
        # return the last elem. This is bottom up approach
        res = dp[m-1][n-1][1]
        return  res % (10**9 + 7) if res>=0 else -1
                    
                    
        
        