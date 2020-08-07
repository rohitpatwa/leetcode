# 2 ways to solve [dp, maths]. dp[i][j] = dp[i-1][j] + dp[i][j-1].

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                temp = 0
                if i-1>=0:
                    temp += dp[i-1][j]
                
                if j-1>=0:
                    temp += dp[i][j-1]
                    
                dp[i][j] += temp

        return dp[-1][-1]




# Maths approach

def uniquePaths(self, m: int, n: int) -> int:
    if m==1  or  n==1:
        return 1
    x = m + n
    fac = [1] * (x+2)
    fac[1] = 1
    for i in range ( 1 , x+1 ) :
        fac[i] = fac[i-1] * i
        
    return int ( fac[m-2+n] / ( fac[m-1] * fac[n-1] ) )