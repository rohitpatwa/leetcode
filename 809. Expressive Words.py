# Find run-length-encoding of S and all query words. Then simply compare the run length encodings with a number of checks.

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        if not S or not words:
            return 0
        
        res = 0
        s_rle = self.RLE(S)

        for w in words:

            w_rle = self.RLE(w)
            if len(w_rle) != len(s_rle):
                continue
            
            flag = True    
            for x, y in zip(w_rle, s_rle):
                if (x[0]==y[0]) and (  (x[1]==y[1]) or ( x[1]<y[1] and y[1]>=3 )  ):
                    continue
                else:
                    flag = False
                    break
                    
            if flag:
                res += 1
                
        return res
                
            
                    
    def RLE(self, word):
        rle = []
        c = word[0]
        j = 1
        for i in range(1, len(word)):
            if word[i] == c:
                j += 1
            else:
                rle.append([c, j])
                j = 1
                c = word[i]

        rle.append([c, j])

        return rle