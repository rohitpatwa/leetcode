# Maintain the direction while traversing. Keep track of top, right, bottom and left limits of the matrix. Iterate til l<=r and t<=b.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        res = []
        m, n = len(matrix), len(matrix[0])
        
        d = 0
        t, r, b, l = 0, n-1, m-1, 0
        
        while (l<=r and t<=b):
            
            if d==0:
                for x in range(l, r+1):
                    res.append(matrix[t][x])
                t += 1
                
            elif d==1:
                for y in range(t, b+1):
                    res.append(matrix[y][r])
                r -= 1
                
            elif d==2:
                for x in range(r, l-1, -1):
                    res.append(matrix[b][x])
                b -= 1
                
            else:
                for y in range(b, t-1, -1):
                    res.append(matrix[y][l])
                l += 1
        
            d = (d+1)%4
        
        return res