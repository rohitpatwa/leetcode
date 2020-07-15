# Two pointer approach. Initiate i, j = 0, 1. Keep i on even terms, j on odd. Increment by 2 if correct, else swap.

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        i, j = 0, 1
        
        while i<len(A) and j<len(A):
            # is is for even and j is for odd
            
            if A[i]%2==0:
                i += 2
                continue
            if A[j]%2!=0:
                j += 2
                continue
            
            A[i], A[j] = A[j], A[i]
        return A
                               
