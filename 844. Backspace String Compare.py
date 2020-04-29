# Iterate on reversed strings. If #, skip+=1, else skip-=1. Compare after skips. If both pointers overflow, return True, else return False.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        n1, n2 = len(S), len(T)
        S, T = S[::-1], T[::-1]
        i, j = 0, 0

        while i<n1 or j<n2:
            skipS, skipT = 0, 0

            while i<n1 and (skipS or S[i]=='#'):
                if S[i]=='#':
                    skipS += 1
                else:
                    skipS -= 1
                i += 1

            while j<n2 and (skipT or T[j]=='#'):
                if T[j]=='#':
                    skipT += 1
                else:
                    skipT -= 1
                j += 1

            if i>=n1 and j>=n2:
                return True
            elif (i>=n1 and j<n2) or (j>=n2 and i<n1):
                return False
            elif S[i] != T[j]:
                return False
            i += 1
            j += 1

        if i>=n1 and j>=n2:
            return True
        return False
