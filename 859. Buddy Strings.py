# Check for both conditions, when A equals B and not.When equal, there should be 2 elements to swap. When not, diff should be 2.

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False

        ctr_a, ctr_b = Counter(A), Counter(B)
        if A==B:
            if max(ctr_a.values())==1:
                return False
            return True
        
        else:
            if ctr_a != ctr_b:
                return False
            uneq = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    uneq += 1
                    
            return uneq==2