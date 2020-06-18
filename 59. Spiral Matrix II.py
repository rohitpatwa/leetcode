 : 

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0]*n for _ in range(n)]
        
        d = 0
        t, r, b, l = 0, n-1, n-1, 0
        ctr = 1
        while t<=b and l<=r:
            if d==0:
                for x in range(l, r+1):
                    res[t][x] = ctr
                    ctr += 1
                t += 1
                
            elif d==1:
                for y in range(t, b+1):
                    res[y][r] = ctr
                    ctr += 1
                r -= 1
            
            elif d==2:
                for x in range(r, l-1, -1):
                    res[b][x] = ctr
                    ctr += 1
                b -= 1
            
            else:
                for y in range(b, t-1, -1):
                    res[y][l] = ctr
                    ctr += 1
                l += 1
            
            d = (d+1)%4
        
        return res
                    
                