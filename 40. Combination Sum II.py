# Similar to finding subsets problem. Here find subsets whose sum is equal to target. Sort candidates and skip repeat numbers.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = sorted(candidates)
        self.helper(0, [], target)
        return self.res
    
    def helper(self, idx, curr, target):
        if target==0:
            self.res.append(curr[:])
            return 
        
        if target < 0:
            return 
        
        for i in range(idx, len(self.candidates)):
            # To avoid repeated numbers in the answer
            if i==idx or self.candidates[i]!=self.candidates[i-1]:
                curr.append(self.candidates[i])
                self.helper(i+1, curr, target-self.candidates[i])
                curr.pop()
