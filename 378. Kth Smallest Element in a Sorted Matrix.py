# Create a max heap of size k. At every element smaller than top of heap, replace it with top. At the end, return top.

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        h = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(h) < k:
                    heapq.heappush(h, -matrix[i][j])
                elif -h[0] > matrix[i][j]:
                    heapq.heappop(h)
                    heapq.heappush(h, -matrix[i][j])
                
        return -h[0]