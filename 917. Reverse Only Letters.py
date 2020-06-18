# Use two pointer approach - i at the start, j at the end. Swap the chars at i and j while i<j.

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j = 0, len(S) - 1
        S = list(S)
        while i<j:
            if S[i].lower() == S[i].upper():
                i += 1
            elif S[j].lower() == S[j].upper():
                j -= 1
            else:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        return ''.join(S)