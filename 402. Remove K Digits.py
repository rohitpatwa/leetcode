# Push nums in a stack. When a smaller number appears, keep poppig the prev num and then push the num provided k>0. Remove duplicate nums and remove leading 0s.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k == len(num):  # remove all numbers and return 0
            return '0'
        
        S = []  # stack
        for n in num:
            while S and k>0 and int(S[-1]) > int(n): # this is a while loop and not if condition
                S.pop()  # pop num if we find a smaller num
                k -= 1
            S.append(n)
        
        while k>0:  # all remaining nums are equal
            S.pop()
            k -= 1
                
        i = 0
        while i<len(S)-1 and S[i]=='0':  # remove leading zeros
            i += 1
        
        return ''.join(S[i:])
        
