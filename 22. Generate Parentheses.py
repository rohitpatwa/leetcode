# Open parenthesen < n and closed parantheses < open. Keep recursing and backtrackting to generate all combinations.

def generateParenthesis(self, n: int) -> List[str]:
        
        self.res = []
        self.n = n
        self.helper("", 0, 0)
        return self.res
    
    def helper(self, curr, start, end):
        if len(curr)==2*self.n:
            self.res.append(curr)
            return
        
        if start < self.n:
            self.helper(curr + "(", start+1, end)
            
        if end < start:
            self.helper(curr + ")", start, end + 1)