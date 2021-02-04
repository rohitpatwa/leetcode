# Create a Q and a set S. Append (m, t ) in Q and add m in S. Whenever a new message comes, remove all the t-10 messages from Q and S and then add new one.

from collections import deque

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Q = deque()
        self.S = set()
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while self.Q:
            m0, t0 = self.Q[0]
            if t0 <= timestamp-10:
                self.Q.popleft()
                self.S.remove(m0)
            else:
                break

        if message in self.S:
            return False
        else:
            self.Q.append([message, timestamp])
            self.S.add(message)
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)