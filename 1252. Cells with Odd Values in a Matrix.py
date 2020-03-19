# Create two lists of zeros; rows and cols. Keep incrementing count in the lists. Increment total_odd by r+c%2==1

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        rows, cols = [0]*n, [0]*m 
        
        for i in indices:
            rows[i[0]] += 1
            cols[i[1]] += 1
            
        count = 0
        for r in rows:
            for c in cols:
                if (r+c)%2==1:
                    count += 1
        return count