# Iterate on the digits from the end to beginning. Update the digit and c bit on each iteration.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i], c = (digits[i]+c)%10, (digits[i]+c)//10
            
        if c==1:
            digits = [1] + digits
        
        return digits
            