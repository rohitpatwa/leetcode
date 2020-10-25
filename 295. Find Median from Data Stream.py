# Use minheap and maxheap. Pushpop every new elem in maxheap, add popped elem in min heap. If len(minheap)>len(maxheap), re-balance.

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.minH = []  # will store upper half of data
        self.maxH = []  # will store lower half of data

    def addNum(self, num: int) -> None:
        self.count += 1  # count elems to know if num elems are odd or even 
        
        # Add every new elem to max heap and pop the largest
        x = heapq.heappushpop(self.maxH, -num)
        
        # Add the popped elem in the min heap
        heapq.heappush(self.minH, -x)
        
        # If len min_heap > len max_heap, pop smallest from min heap and add
        # it to max_heap. This way, at any point, len of max_heap will be gte len 
        # of min_heap.
        if len(self.minH) > len(self.maxH):
            x = heapq.heappop(self.minH)
            heapq.heappush(self.maxH, -x)
        
        

    def findMedian(self) -> float:
        if self.count%2==0:
            return (self.minH[0] - self.maxH[0])/2
        return -self.maxH[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()