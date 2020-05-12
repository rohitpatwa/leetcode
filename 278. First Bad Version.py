# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        
        while l<r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m # Because m can be the first bad version, we keep it in the limits
            else:
                l = m+1 # Because m is not a bad version, we do not keep it in the limits
        return l