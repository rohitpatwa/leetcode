# dp=[]*len(n+1). dp[i] means no. of ways to decode string of len i. Get single and double from s. single>0: dp[i]+=dp[i-1]; 10<=double<=26: dp[i]+=dp[i-2].

class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 if s[0]=="0" else 1
        
        # dp[i] means total number of ways to decode string of len i
        
        for i in range(2, n+1):
            single = int(s[i-1])
            double = int(s[i-2:i])
            
            if single > 0:
                dp[i] += dp[i-1]
                
            if 10 <= double <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
        