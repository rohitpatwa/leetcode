# Every arr[i][j] = arr[i-1][j] + arr[i-1][j-1]. Handle corner cases

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        
        res = [[1]]
        
        for itr in range(1, numRows):
            temp = []
            j = 0
            while j+1 < len(res[-1]):
                temp.append(res[-1][j] + res[-1][j+1])
                j += 1
            temp = [1] + temp + [1]
            res.append(temp)
            
        return res