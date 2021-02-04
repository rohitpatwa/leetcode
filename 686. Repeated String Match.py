# min_res = ceil(lenB/lenA). Check only 2 values for k i.e. min_res and min_res+1. if B not in A*k, return -1.

import math

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        max_res = math.ceil(len(B)/len(A))
        
        for i in range(max_res, max_res+2):
            if B in A*i:
                return i
        return -1