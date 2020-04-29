# Use two pointers, one at beginning, one at end. Run 2 while loops inside a one while loop to skip all non alphanumeric charectes

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0, len(s)-1
        if not s:
            return True
        s = s.lower()
        while True:
            while i<j and not self.is_valid(s[i]):
                i += 1
                
            while i<j and not self.is_valid(s[j]):
                j -= 1
            
            if i>=j:
                return True
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
        
    def is_valid(self, c):
        
        if (ord(c) >= 48 and ord(c)<=57) or (ord(c) >=97  and ord(c)<=122):
            return True
        return False