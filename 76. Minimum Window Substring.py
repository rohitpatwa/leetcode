# Get counter of t. Then iterate over s using 2 pointers (i, j). In each step forward of j, move i as many steps as possible.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        t_freq = Counter(t)
        s_freq = {}
        
        res, min_len = "", float('inf')
        i, j = 0, 0
        
        num_left = len(t_freq.keys())
        
        
        while j<len(s):
            char = s[j]

            s_freq[char] = s_freq.get(char, 0) + 1
            
            if t_freq[char] == s_freq[char]:
                num_left -= 1
                
            
            while num_left==0:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    res = s[i:j+1]
                
                char = s[i]
                
                s_freq[char] -= 1

                if char in t_freq and t_freq[char] > s_freq[char]:
                    num_left += 1

                i += 1

            j += 1

        return res