# Create a number with reversed digits. Compare the two numbers.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        rev = 0
        y = x
        
        while y>0:
            digit = y%10
            y /= 10
            rev = 10*rev + digit
            
        if rev==x:
            return True
        return False