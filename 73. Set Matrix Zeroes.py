# Check if 0th row and col contains 0. Iterate over indices and store zeros in (i,0) and (0,j). Propagate zeros from row0 and col0; start iteration from index 1.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
                
        rows = [0]*m
        cols = [0]*n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows[i] = 1
                    cols[j] = 1
                
        for i in range(m):
            if rows[i]:
                for x in range(n):
                    matrix[i][x] = 0
        
        for j in range(n):
            if cols[j]:
                for x in range(m):
                    matrix[x][j] = 0
        
        return matrix



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        
    
        first_row_zero = False
        first_col_zero = False
        for j in range(n):
            if matrix[0][j]==0:
                first_row_zero = True
                break
                
        for i in range(m):
            if matrix[i][0]==0:
                first_col_zero = True
                break
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if matrix[i][0]!=0:
                        matrix[i][0]=0
                    if matrix[0][j]!=0:
                        matrix[0][j]=0
        
        for i in range(1,m):
            if matrix[i][0]==0:
                for x in range(n):
                    matrix[i][x] = 0
        
        
        for j in range(1, n):
            if matrix[0][j]==0:
                for x in range(m):
                    matrix[x][j] = 0
        
        if first_row_zero:
            for j in range(n):
                matrix[0][j]=0
                
        if first_col_zero:
            for i in range(m):
                matrix[i][0]=0
        
        return matrix