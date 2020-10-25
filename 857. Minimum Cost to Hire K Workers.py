# Sort on (wage/quality). Create a max heap on quality of size k. Iterate on sorted w_q list, ans = sum(qualities)*current_ratio. Keep updating.

import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = [[w/q, w, q] for (w,q) in zip(wage, quality)]
        
        workers = sorted(workers)
        
        heap = []
        
        ans = float('inf')
        sum_qualities = 0
        
        for ratio, wage, quality in workers:
            heapq.heappush(heap, -quality)
            sum_qualities += quality
            
            if len(heap) > K:
                sum_qualities += heapq.heappop(heap)
                
            if len(heap) == K:
                ans = min(ans, sum_qualities*ratio)
                
        return ans