# One pass solution. d=[0]*10 for 10 digits. If s==g:b+=1;else: every secret key digit increases d[s]. If we find d[s]<0 that means it has been guessed so c+=1.

      

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = [0]*10
        b, c = 0, 0
        for i in range(len(secret)):
            s, g = int(secret[i]), int(guess[i])
            
            if s==g:
                b += 1
            else:
                if d[s] < 0:
                    c += 1
                if d[g] > 0:
                    c += 1
                d[s] += 1
                d[g] -= 1
        return f'{b}A{c}B'