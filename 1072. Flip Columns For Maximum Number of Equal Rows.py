# Create a dict of patterns. Add tuple(row) and tuple(row_compliment) to dict. Return max(dict.vals()).

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = {}
        
        for row in matrix:
            pattern[tuple(row)] = pattern.get(tuple(row), 0) + 1
            
            flip = [1-x for x in row]
            
            pattern[tuple(flip)] = pattern.get(tuple(flip), 0) + 1
            
        return max(pattern.values())