# Look at 1 bit (b) at a time(right to left) and maintain a carry (c). (b=0,c=0->1,c=0), (b=0,c=1->2, c=1) and so on.

class Solution:
    def numSteps(self, s: str) -> int:
        
        s = s[::-1]
        count, c, i = 0, 0, 0
        
        for i in range(len(s)-1):
            if c==0:
                if int(s[i])==0:
                    count += 1
                else:
                    count += 2
                    c = 1
            else:
                c = 1
                if int(s[i])==0:
                    count += 2
                else:
                    count += 1
        if c==0:
            return count
        else:
            return count+1