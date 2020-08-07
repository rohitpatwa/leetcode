# Simulate picking and not picking every element within a heler function. Pick next value, recurse, backtrack. Add every combi to res.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.generate_subsets([], 0)
        return self.res
    
    def generate_subsets(self, curr, idx):
        
        self.res.append(curr[:])
        
        for i in range(idx, len(self.nums)):
            curr.append(self.nums[i])
            self.generate_subsets(curr, i+1)
            curr.pop()