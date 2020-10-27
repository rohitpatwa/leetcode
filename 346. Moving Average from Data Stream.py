# Keep a queue of size k. Keep pushing numbers until capacity and return average.

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.Q = deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.Q) == self.size:
            self.Q.popleft()
        self.Q.append(val)
        return sum(self.Q)/len(self.Q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)