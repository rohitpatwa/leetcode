# At each step, number of ways to climb is equal to (dp[i-1] + dp[i-2]). We can take 1 step from i-1 and 2 steps from i-2.

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]