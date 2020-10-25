# Create a list named dp. dp[i] means if or not we can reach char i using wordDict. Run 2 pointers on s. If dp[j] and s[j:i] in wordDict: dp[i]=True.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        
        wordDict = set(wordDict)
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
        
        