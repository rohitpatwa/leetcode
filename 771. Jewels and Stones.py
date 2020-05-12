# Create a counter over S. Then iterate over J adding counts from dict of S.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        for c in S:
            d[c] = d.get(c, 0) + 1
        
        count = 0
        for c in J:
            count += d.get(c, 0)
        return count