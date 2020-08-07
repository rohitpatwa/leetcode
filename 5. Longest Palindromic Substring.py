# Iterate through the array, at each step expand from middle and find longest palindrome. Cover odd and even cases of plaindromes.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end, max_len = 0, 0, 1
        
        for i in range(len(s)):
            len1, l1, r1 = self.expand(s, i, i)
            len2, l2, r2 = self.expand(s, i, i+1)
            
            if len1>=len2 and len1>max_len:
                start, end = l1, r1
                max_len = len1
            elif len2>=len1 and len2>max_len:
                start, end = l2, r2
                max_len = len2
        
        return s[start:end+1]
        
        
    def expand(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        
        return r-l-1, l+1, r-1