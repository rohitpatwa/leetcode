# Find the next biggest power of 2. Return 2**power - num.

class Solution:
    def findComplement(self, num: int) -> int:
        n = bin(num)[2:]
        inverted = ''.join([['1', '0'][int(x)] for x in n])
        return int(inverted, 2)
    
class Solution:
    def findComplement(self, num: int) -> int:
        base = 1
        
        for i in range(1, 32):
            if 2 ** i - 1 >= num:
                base = 2 ** i - 1
                break
                
        return base - num