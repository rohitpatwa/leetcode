# Check if 1st row or 1st col contains any 1. If yes max_sq=1 else 0. Iterate over (1, m) and (1, n) elements. arr[i,j]=min(arr[i,j-1], arr[i-1,j-1], arr[i, j-1]) + 1.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_sq = 0
        
        for i in range(m):
            if max_sq or matrix[i][0]=="1":
                max_sq = 1
                break
                
        for j in range(n):
            if max_sq or matrix[0][j]=="1":
                max_sq = 1
                break
        

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]=="1":
                    matrix[i][j] = min([
                                        int(matrix[i-1][j]), 
                                        int(matrix[i-1][j-1]), 
                                        int(matrix[i][j-1])
                                    ]) + 1
                    max_sq = max(max_sq, matrix[i][j])

        return max_sq**2