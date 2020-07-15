# Perform a normal binary search. Do division and modulus when accessing the elements of the matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        low, high = 0, (m*n)-1
        
        while low<=high:
            mid = (low+high)//2
            
            r = mid // n
            c = mid % n
            
            if target==matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                high = mid - 1
            else:
                low = mid + 1
                
        return False