# Precompute the max_width at each point. Then iterate over each idx, go down, update and add max_width to res.

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n  = len(mat), len(mat[0])
        
        dp = [[0]*n for _ in range(m)]
        
        
        # This step is pre-computation
        # It's storing the max_width of all rectangles fixed at that point
        for i in range(m):
            c = 0
            for j in range(n-1, -1, -1):
                if mat[i][j] == 1:
                    c += 1
                else:
                    c = 0
                dp[i][j] = c
                
        res = 0
        for i in range(m):
            for j in range(n):
                max_width = dp[i][j]
                
                for h in range(i, m):
                    max_width = min(max_width, dp[h][j])
                    if max_width==0:
                        break
                    res += max_width
                    
        return res