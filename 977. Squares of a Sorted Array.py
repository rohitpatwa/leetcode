# Find the point where -ve +ve transition takes place. From that point, use two pointers i,j. if abs(i)<abs(j); res.append(i**2); i-=1

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []
        
        
        j = 0
        while j<len(A) and A[j]<0:
            j += 1
        i = j-1
        
        res = []
        while i>=0 and j<len(A): 
            
            if abs(A[i])>=A[j]:
                res.append(A[j]**2)
                j += 1
            else:
                res.append(A[i]**2)
                i -= 1
        while i>=0:
            res.append(A[i]**2)
            i -= 1
        while j<len(A):
            res.append(A[j]**2)
            j += 1
        return res