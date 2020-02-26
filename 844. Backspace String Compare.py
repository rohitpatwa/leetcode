# Update S and T by deleting chars as per #. Compare S and T.

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        
        i = 0
        while i < len(S):
            if S[i] == '#':
                S = S[:max(0, i-1)] + S[i+1:]
                i = max(0, i-1)
            else:
                i += 1

        i = 0
        while i < len(T):
            if T[i] == '#':
                T = T[:max(0, i-1)] + T[i+1:]
                i = max(0, i-1)
            else:
                i += 1

        return S==T