# Use a Q to keep recent timestamps. Whenever ping is called, add t to Q and remove all the expired ones. Return len(Q)

class RecentCounter:

    def __init__(self):
        self.Q = []
        

    def ping(self, t: int) -> int:
        self.Q.append(t)
    
        while self.Q[0]<t-3000:
            self.Q.pop(0)
        
        return len(self.Q)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)