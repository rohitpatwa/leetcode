# Append 1 in each iteration. row[j] = row[j] + row[j-1] in reverse order.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        
        row = [1]        
        for i in range(1, rowIndex+1):
            row.append(1)
            for j in range(i-1, 0, -1):
                row[j] = row[j] + row[j-1]
        return row
            