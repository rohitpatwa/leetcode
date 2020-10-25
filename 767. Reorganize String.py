# Create list of len(S). Create Counter. Iterate from most freq to least. keep inserting in alternate idx(0,2,4 ...). when i>=len(S): i=1.

import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        
        counter = Counter(S)

        # Sorted ascending on counts
        val_char = sorted([(v, k) for (k, v) in counter.items()])
        
        max_occur = val_char[-1][0]
        if max_occur > (len(S)+1)/2:
            return ""
        
        res = [""]*len(S)
        
        i = 0
        while val_char:
            count, char = val_char.pop()
            
            for j in range(count):
                res[i] = char
                i += 2
                
                if i>=len(S):
                    i = 1
        return "".join(res)