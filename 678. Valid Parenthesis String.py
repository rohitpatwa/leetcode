# Iterate s once from l->r and r->l. left_bal and right_bal in s. If at any point left_bal<0 or right_bal<0; return False; else return True.

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_bal, right_bal = 0, 0
        n = len(s)

        for i in range(len(s)):
            if s[i] in '(*':
                left_bal += 1
            else:
                left_bal -= 1
        
        
            if s[n-1-i] in '*)':
                right_bal += 1
            else:
                right_bal -= 1
        
        
            if left_bal<0 or right_bal<0:
                return False
        return True
