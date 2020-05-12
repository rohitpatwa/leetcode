# Create a counter on magazine str. Iterate over note str and keep subtracting from the counter. 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1
            
        for c in ransomNote:
            if c in d and d[c] >= 1:
                d[c] -= 1
            else:
                return False
        return True