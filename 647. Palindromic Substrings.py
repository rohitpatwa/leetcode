# Iterate over the str and in each itr call expand(i, i) and expand(i, i+1). In expand func, expand on right and left and count palindromes.

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += self.expand(s, i, i)  # Even len palindrome
            count += self.expand(s, i, i+1)  # Odd len palindrome
        return count
        
        
    def expand(self, s, i, j):
        count = 0
        while i>=0 and j<len(s) and s[i]==s[j]:
            count += 1
            i -= 1
            j += 1
        return count