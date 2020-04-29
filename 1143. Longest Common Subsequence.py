# Create a 2D table of dim(m+1, n+1). if x[i]==y[j] => LCS(i, j)=LCS(i-1, j-1) + 1; Otherwise LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1))


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]