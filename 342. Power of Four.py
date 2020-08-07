# Binary representation should be of the form 1000... and of odd length.

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<0: return False
        if num==1: return True
        
        s = bin(num)[2:]
        if set(s[1:]) == {'0'} and len(s)%2==1:
            return True
        return False