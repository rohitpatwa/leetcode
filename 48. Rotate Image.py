# Repear n/2 iterations. Replace 4 points in one go.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        iterations = n//2
        
        for itr in range(iterations):
            for offset in range(itr, n - itr -1):
                og_coord_1 = matrix[itr][offset]
                og_coord_2 = matrix[offset][n - 1 - itr]
                og_coord_3 = matrix[n - 1 - itr][n - 1 - offset]
                og_coord_4 = matrix[n - 1 - offset][itr]
                
                
                matrix[itr][offset] = og_coord_4
                matrix[offset][n - 1 - itr] = og_coord_1
                matrix[n - 1 - itr][n - 1 - offset] = og_coord_2
                matrix[n - 1 - offset][itr] = og_coord_3
        return matrix


# Based on flips => Beautiful solution

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         for i, row in enumerate(zip(*matrix)):
#             matrix[i] = list(row[::-1])
#         return matrix