# Maintain a count variable. Every time we go insise a folder, cnt++, every time we go back from a folder cnt--.

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for l in logs:
            if l=="../":
                count = max(0, count-1)
            elif l=='./':
                pass
            else:
                count += 1
        return count