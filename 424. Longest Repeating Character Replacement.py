# Sliding window problem. Keep increasing end. max_count=max char inside window. If (end-start+1 - max_count > k): start += 1.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # We create char_counts to keep counts of characters within window
        char_counts = {chr(x+ord('A')):0 for x in range(26)}
        
        window_start, max_count, max_len = 0, 0, 0
        
        for window_end in range(len(s)):
            curr_char = s[window_end]#ord(s[window_end]) - ord('A')
            char_counts[curr_char] += 1
            
            # max number of repeating chars within the window.
            # We keep a track of these because we will replace all other 
            # chars except the char with max count
            max_count = max(max_count, char_counts[curr_char])
            
            while window_end - window_start + 1 - max_count > k:
                char_counts[s[window_start]] -= 1
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)

        return max_len