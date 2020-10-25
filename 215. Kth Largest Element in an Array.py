# Create a min heap of size k. While inserting elements, if num > heap.top, heap.pop, insert num. Else pass. Return heap.top.

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for i in nums:
            if len(h) < k:
                heapq.heappush(h, i)
            else:
                heapq.heappushpop(h, i)
        return heapq.heappop(h)