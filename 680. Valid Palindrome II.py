# Use 2 pointers initially. When diff chars seen at i and j, call checkPslindrome with both cases i.e. skip ith, skip jth. If either satisfies, return True.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s)-1
        while i<j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return self.isPalindrome(s[i+1:j+1]) or self.isPalindrome(s[i:j]) 
        return True
    
    def isPalindrome(self, a):
        return a==a[::-1]