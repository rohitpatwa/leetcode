# Remove special chars except the sign char. Convert to int and return the number with min/max with limit number.

import re

class Solution:
    def myAtoi(self, str: str) -> int:
        
        x = re.sub(r'^\s*([+-]?\d+)?.*', r'\1', str)
        if not x:
            return 0
        x = int(x)
        if x>0:
            return min(2**31-1, x)
        return max(-2**31, x)