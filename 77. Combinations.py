# Same as subsets problem. Just put a constraint to add subsets of len 2 and return after adding because we don't want to explore subsets of len > 2.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.combinations(res, 1, n, k, [])
        return res
    
    def combinations(self, res, idx, n, k, curr):
        
        if len(curr)==k:
            res.append(curr[:])
            return
        
        for i in range(idx, n+1):
            curr.append(i)
            self.combinations(res, i+1, n, k, curr)
            curr.pop()
            