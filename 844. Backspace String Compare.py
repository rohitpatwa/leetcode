# Use S_skip and T_skip pointers to remember the skips. Within each while loop, perform the skips in S and T and then compare the character.

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        
        i, j = len(S) - 1, len(T) - 1
        ih, jh = 0, 0
        
        while i >= 0 or j >= 0:
            if i >= 0 and (ih > 0 or S[i] == '#'):
                if S[i] == '#': 
                    ih += 1
                else: 
                    ih -= 1
                i -= 1
                continue
            if j >= 0 and (jh > 0 or T[j] == '#'):
                if T[j] == '#': 
                    jh += 1
                else: 
                    jh -= 1
                j -= 1
                continue

            s = '@' if i < 0 else S[i]
            t = '@' if j < 0 else T[j]
            if s != t: return False
            else: 
                i -= 1 
                j -= 1
        
        return True