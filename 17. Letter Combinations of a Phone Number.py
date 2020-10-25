# Perform DFS. Create a number to char mapping. Call a helper function on each digit and iterate through it's chars recursively.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.digits = digits
        self.map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.helper(0, '', res)
        return res
        
    def helper(self, i, curr, res):
        if i == len(self.digits):
            res.append(curr)
            return 
        
        for c in self.map[self.digits[i]]:
            self.helper(i+1, curr+c, res)
            