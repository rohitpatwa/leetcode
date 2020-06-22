# Solution is brute force. Go through each number and check if it is self dividing.

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            if self.is_self_dividing(i):
                res.append(i)
        return res
    
    def is_self_dividing(self, i):
        digits = list(map(int, list(str(i)) ))
        if 0 in digits:
            return False
        return all([i%x==0 for x in digits])