# 2 pointer soluion(l, r). Keep latest occ of every char in dict. If curr char in dict, l = d[c] + 1. Update max at each step.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char2idx = {}
        left, max_len = 0, 0
        
        for right, char in enumerate(s):
            
            if char in char2idx:
                left = max(left, char2idx[char] + 1)

            char2idx[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len