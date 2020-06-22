# Use global_freq and local_freq to keep a count of repeating chars.

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        
        freq = [99999]*26
        
        for w in A:
            local_freq = [0]*26
            for c in w:
                local_freq[ord(c) - ord('a')] += 1
            for i in range(26):
                freq[i] = min(freq[i], local_freq[i])
        
        
        res = []
        for i in range(26):
            if freq[i]:
                res += list(chr(ord('a') + i) * freq[i])
                
        return res

    