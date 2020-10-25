class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        # This dictionary will store the last known occurence of every char
        d = {}
        for i, c in enumerate(S):
            d[c] = i
            
        
        res = []  # This will store the result i.e. len of each substr
        count = 0  # This will store len of curr substr
        i = 0  # This will be used to iterate over S
        
        while i<len(S):
            max_len = d[S[i]]  # set max_len to last occ of d[S[i]]
            count = 1  # count of curr substr is 1, cuz it contains S[i] already
            
            while i<max_len:
                
                # since i is LESS THAN max_len, we can include next char and update max_len
                i += 1
                max_len = max(max_len, d[S[i]])
                count += 1  
                
            res.append(count)
            i += 1  # chars till i are included so from i+1
            
        return res
            
            
            
            