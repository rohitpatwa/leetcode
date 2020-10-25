# Iterate s and create cand. Add cand to seen set. Recursively call helper. max = max(max, helper() + 1) and backtrack.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = self.helper(s, set())
        return res
    
    def helper(self, s, seen):
        maximum = 0
        for i in range(1, len(s) + 1):
            cand = s[:i]
            if cand not in seen:
                seen.add(cand)
                maximum = max(maximum, self.helper(s[i:], seen) + 1)
                seen.remove(cand)
                
        return maximum