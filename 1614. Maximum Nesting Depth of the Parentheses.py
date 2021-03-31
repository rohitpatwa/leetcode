# Increase depth on open bracket and decrease depth on close bracket. Update result on each iteration.

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        res = 0
        for c in s:
            if c=="(":
                depth += 1
            elif c==")":
                depth -= 1
            res = max(res, depth)
        return res