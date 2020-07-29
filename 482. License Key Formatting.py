# Remove all the -. Start from the end and keep adding each elem to new string. After every k chars, add -. Return res.strip('-')

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        S = S.replace('-', '').upper()
        l = len(S)
        res = ""

        for i in range(l-1, -1, -1):
            res += S[i]
            if (l-i) % K == 0:
                res += '-'

        return res.strip('-')[::-1]